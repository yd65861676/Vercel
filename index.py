from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# 配置密钥（在生产环境中应使用环境变量）
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-dev-key')

@app.route('/')
def home():
    """首页路由"""
    return "Hello from Vercel! 数字艺术市场欢迎您！"

@app.route('/about')
def about():
    """关于页面路由"""
    return "关于我们 - 数字艺术市场"

@app.route('/gallery')
def gallery():
    """艺术品展示页面"""
    # 这里可以从数据库获取艺术品列表
    artworks = [
        {'id': 1, 'title': '星空', 'artist': '艺术家A'},
        {'id': 2, 'title': '海洋', 'artist': '艺术家B'},
        {'id': 3, 'title': '山脉', 'artist': '艺术家C'}
    ]
    return {"title": "艺术品展示", "artworks": artworks}

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """联系页面路由"""
    if request.method == 'POST':
        # 处理表单提交
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # 这里可以添加发送邮件或保存到数据库的逻辑
        
        return redirect(url_for('thank_you'))
    
    return "联系我们 - 数字艺术市场"

@app.route('/thank-you')
def thank_you():
    """表单提交后的感谢页面"""
    return "谢谢您的留言！"

# Vercel Serverless Functions入口点
# 不要在此处添加app.run()，Vercel会自动处理
