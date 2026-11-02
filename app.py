import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # 自動讀取 Render 指派的 Port，若在本機執行則預設使用 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)