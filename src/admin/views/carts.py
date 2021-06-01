from flask import render_template, request, url_for, session, redirect, flash, Blueprint

import datetime

from lib.models import Book, History, User

from lib.db import db

from .login import login_check

cart = Blueprint('carts', __name__)

# ログインチェック
@cart.route('/')
@login_check
def check_cart():
    return render_template('carts/index.html')

# カート画面を表示
@cart.route('/cart')
@login_check
def index():
    cart=session.get('cart')
    cart_details = list()
    if type(cart) is dict:
        for key, value in cart.items():
            book=Book.query.get(key)
            cart_details.append({ 'id':key, 'name':book.name, 'title':book.title, 'category':book.category })
    return render_template('carts/index.html',cart_details=cart_details)

@cart.route('/create',methods=['POST'])
@login_check
def create():
    book_id=request.form.get('book_id') or ""
    cart=session.get('cart')
    if type(cart) is dict:
        cart[book_id]=Book.query.get(book_id).title
    else:
        cart={book_id:Book.query.get(book_id).title}
    session['cart']=cart
    flash('カートに追加しました','success')
    return redirect(url_for('carts.index'))

@cart.route('/<string:book_id>/delete',methods=['POST'])
@login_check
def delete(book_id):
    if book_id=='all':
        session.pop('cart',None)
    else:
        cart=session.get('cart')
        cart.pop(book_id,None)
        session['cart']=cart
    flash('商品が削除されました','success')
    return redirect(url_for('carts.index'))

@cart.route('/insert')
@login_check
def insert():
    carts = session.get('cart')
    user_id = session.get('user_table_id')
    for book_id, title in carts.items():
        
        if book_id and title:
            
            history = History(
                book_id = book_id,
                user_id = user_id,
                datetime = datetime.date.today()
            )

            undergraduate = User.query.get(user_id).undergraduate
            if undergraduate == '経済学部':
                Book.query.get(book_id).keizai += 1
            elif undergraduate == '法学部':
                Book.query.get(book_id).hougaku += 1
            elif undergraduate == '理学部':
                Book.query.get(book_id).rigaku += 1
            elif undergraduate == '工学部':
                Book.query.get(book_id).kougaku += 1
            elif undergraduate == '文学部':
                Book.query.get(book_id).bungaku += 1
            elif undergraduate == '医学部':
                Book.query.get(book_id).igaku += 1

            db.session.add(history)
            db.session.commit()

        else:
            flash('最初からやり直してください', 'error')

    session.pop('cart', None)
    flash('商品を借りました', 'success')
    return redirect(url_for('carts.index'))