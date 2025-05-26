from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Vercel! 这是一个根目录测试。"

@app.route('/test')
def test():
    return "测试路由正常工作！"
