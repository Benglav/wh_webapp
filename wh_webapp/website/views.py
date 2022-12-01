from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Product
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        product = request.form.to_dict()

        if len(product.get('productInput')) < 3:
            flash('Product name is too short!', category='error')
        elif not product.get('productInput').isalpha():
            flash('only use A-Z characters, try again.', category='error')
        else:
            new_product = Product(name=product.get('productInput'), price = product.get('productPrice'), user_id=current_user.id)

            db.session.add(new_product)
            db.session.commit()
            flash('Product added!', category='success')
    return render_template('home.html', user=current_user)


@views.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    if request.method == 'POST':
        product_search = request.form.get('productSearch')
        try:
            product_search.isalpha()
            product = Product.query.filter_by(name=product_search).first()
        except:
            flash('only use A-Z characters, try again.', category='error')

        try:

            product_name = product.name
            price = product.price
            flash('Product found.', category='success')
            return render_template('search.html', user=current_user, product=product_name, price=price)
        except:
            flash('Product does not exist, try again.', category='error')

    return render_template('search.html', user=current_user)

