from run import app

# Import models from models folder
from models.item import Item
from models.category import Category
from models.user import User

# Import flask functionality
from flask import (render_template,
                   request,
                   redirect,
                   url_for,
                   flash,
                   make_response)

# Import session state from auth_views controler
from auth_view import login_session
import random
import string

# User auth implemnet
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

# for login authtication
def login_required(function):
    @wraps(function)
    def wrapper():
        if 'username' in login_session:
            function()
        else:
            flash('A user must be logged to add a new item.')
            response = make_response(json.dumps(
                "A user must be logged to add a new item."
            ), 401)
            return response
        return wrapper

# Show catalog
@app.route('/')
def showAllitems():
    """
    Create anti-forgery state token
    """
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state

    categories = Category.query.order_by(Category.name).all()
    items = Item.query.order_by(Item.id).limit(10)

    if 'username' not in login_session:
        return render_template('publicCatalog.html',
                               categories=categories,
                               items=items,
                               STATE=state)
    else:
        return render_template('catalog.html',
                               categories=categories,
                               items=items)

# Show item
@app.route('/catalog/<int:item_cat>/<string:item_name>')
def showItem(item_cat, item_name):
    item = Item.query.filter_by(title=item_name).one()
    if 'username' not in login_session:
        return render_template('publicShowItem.html', item=item)
    else:
        return render_template('showitem.html', item=item)

# Show Category items
@app.route('/catalog/<int:category_id>/')
@app.route('/catalog/<int:category_id>/items')
def showCategory(category_id):
    categories = Category.query.order_by(Category.name).all()
    category = Category.query.filter_by(id=category_id).one()
    items = Item.query.filter_by(cat_id=category_id).all()
    items_len = len(items)
    if 'username' not in login_session:
        return render_template('publicShowcategories.html',
                               categories=categories,
                               items=items,
                               category_name=category.name,
                               length=items_len)
    else:
        return render_template('showCategories.html',
                               categories=categories,
                               items=items,
                               category_name=category.name,
                               length=items_len)

# Create a new item
@app.route('/catalog/new', methods=['GET', 'POST'])
@auth.login_required
def newItem():
    categories = Category.query.order_by(Category.name)
    if request.method == 'POST':
        newItem = Item(
            title=request.form['title'],
            cat_id=request.form['category'],
            description=request.form['description'],
            user_id=login_session['user_id'])
        db.session.add(newItem)
        flash('New item %s Successfully Created' % newItem.title)
        return redirect(url_for('showAllitems'))
    else:
        return render_template('newItem.html', categories=categories)

# Edit item
@app.route('/catalog/<string:item>/edit', methods=['GET', 'POST'])
@auth.login_required
def editItem(item):
    categories = Category.query.order_by(Category.name).all()
    editedItem = Item.query.filter_by(title=item).one()
    category = Category.query.filter_by(id=editedItem.cat_id).one()

    if editedItem.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not \
        authorized to edit this Item. Please create your own item in \
        order to edit.');}</script><body onload='myFunction()'>"

    if request.method == 'POST':
        if request.form['title']:
            editedItem.title = request.form['title']
            editedItem.description = request.form['description']
            editedItem.cat_id = request.form['category']
            flash('Item %s Succesfully Edited' % editedItem.title)
            return redirect(url_for('showAllitems'))
    else:
        return render_template('editItem.html',
                               item=editedItem,
                               categories=categories,
                               category=category)

# Delete Item
@app.route('/catalog/<string:item>/delete', methods=['GET', 'POST'])
@auth.login_required
def deleteItem(item):
    itemToDelete = Item.query.filter_by(title=item).one()
    if itemToDelete.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not \
        authorized to delete this Item. Please create your own item in \
        order to delete.');}</script><body onload='myFunction()'>"

    if request.method == 'POST':
        db.session.delete(itemToDelete)
        flash('%s Successfully Deleted' % itemToDelete.title)
        db.session.commit()
        return redirect(url_for('showAllitems'))
    else:
        return render_template('deleteItem.html', item=itemToDelete)
