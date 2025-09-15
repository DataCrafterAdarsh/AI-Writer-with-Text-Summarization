from flask import Flask, render_template, request
from transformers import T5ForConditionalGeneration, T5Tokenizer


app = Flask(__name__)


model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def summarize_text(text, max_length=150, min_length=40):
    """
    Summarizes a given text using a pre-trained T5 model.
    """
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = model.generate(inputs, max_length=max_length, min_length=min_length, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    article_text = request.form['text']
    if article_text:
        summary = summarize_text(article_text)
        return render_template('index.html', summary=summary)
    else:
        return render_template('index.html', summary="Please provide some text to summarize.")

if __name__ == '__main__':
    app.run(debug=True)