import gradio as gr
import pandas as pd
import os
from datetime import datetime

# IMPORT YOUR MAIN PIPELINE
from financial_nlp import bloomberg_pipeline

# -----------------------------
# OUTPUT DIRECTORY (LOCAL FIX)
# -----------------------------
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -----------------------------
# SUMMARY MODE HELPER
# -----------------------------
def get_summary_lengths(mode):
    if mode == "Short":
        return 20, 60
    elif mode == "Medium":
        return 40, 120
    elif mode == "Detailed":
        return 80, 200
    elif mode == "Full Report":
        return 120, 300
    return 40, 120


# -----------------------------
# SINGLE RUN
# -----------------------------
def ui_single_run(text, question, summary_mode):
    try:
        result = bloomberg_pipeline(text, question)

        return f"""
### 💼 Financial NLP Assistant Results

**🔎 Sentiment:** {result['sentiment']}
**📊 Confidence:** {result['confidence']}

---

### 📝 Summary ({summary_mode})
{result['summary']}

---

### ❓ Answer
{result['qa_answer']}
"""
    except Exception as e:
        return f"Error: {str(e)}"


# -----------------------------
# BATCH PROCESSING
# -----------------------------
def ui_batch_run(file, text_col, question_col, summary_mode):
    df = pd.read_csv(file.name)

    results = []

    for idx, row in df.iterrows():
        text = str(row[text_col])
        question = str(row[question_col]) if question_col in df else None

        out = bloomberg_pipeline(text, question)

        results.append({
            "text": text,
            "question": question,
            "sentiment": out["sentiment"],
            "confidence": out["confidence"],
            "summary": out["summary"],
            "qa_answer": out["qa_answer"]
        })

    results_df = pd.DataFrame(results)

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    csv_path = f"{OUTPUT_DIR}/results_{timestamp}.csv"
    results_df.to_csv(csv_path, index=False)

    return results_df, csv_path


# -----------------------------
# GRADIO UI
# -----------------------------
with gr.Blocks(title="Financial NLP Assistant") as demo:

    gr.Markdown("# 💼 Financial NLP Assistant")
    gr.Markdown("Sentiment • Summary • QA • Batch Processing")

    with gr.Tabs():

        # 🔹 SINGLE MODE
        with gr.Tab("Single Analysis"):
            text_in = gr.Textbox(lines=6, label="Financial Text")
            question_in = gr.Textbox(label="Question (optional)")

            summary_mode = gr.Dropdown(
                ["Short", "Medium", "Detailed", "Full Report"],
                value="Medium",
                label="Summary Mode"
            )

            run_btn = gr.Button("Run")
            output = gr.Markdown()

            run_btn.click(
                fn=ui_single_run,
                inputs=[text_in, question_in, summary_mode],
                outputs=output
            )

        # 🧪 BATCH MODE
        with gr.Tab("Batch CSV"):
            file_in = gr.File(label="Upload CSV")
            text_col = gr.Textbox(value="text", label="Text Column")
            question_col = gr.Textbox(value="question", label="Question Column")

            run_batch = gr.Button("Process")
            table_out = gr.DataFrame()
            file_path = gr.Textbox(label="Saved File")

            run_batch.click(
                fn=ui_batch_run,
                inputs=[file_in, text_col, question_col, summary_mode],
                outputs=[table_out, file_path]
            )

demo.launch()