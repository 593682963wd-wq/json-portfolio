"""作者：Wangyuan；日期：2026-10-29；职责：仅合成作品集演示，支持显式JSON内容文件。"""
import json,os
from pathlib import Path
from flask import Flask,render_template,jsonify
from core import run
app=Flask(__name__)
@app.get('/')
def index():
    path=Path(os.environ.get('PORTFOLIO_JSON',str(Path(__file__).parent/'example.json')))
    payload=json.loads(path.read_text(encoding='utf-8'));return render_template('index.html',profile=payload.get('profile',{}),tools=payload.get('tools',[]),stats=run(payload))
@app.get('/healthz')
def health():return jsonify(ok=True)
if __name__=='__main__':app.run(host=os.environ.get('HOST','127.0.0.1'),port=int(os.environ.get('PORT','8091')),debug=False)
