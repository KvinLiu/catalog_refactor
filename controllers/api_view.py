from run import app

from flask import jsonify

from models.category import Category
from models.item import Item

# JSON APIs endpoint to view Catalog Item Information
@app.route('/catalog.json')
def catalogItemJSON():
    """Return all items for a category"""
    categories = Category.query.all()
    sub_categories = [i.serialize for i in categories]
    for i in sub_categories:
        items = Item.query.filter_by(cat_id=i["id"]).all()
        cat_items = [a.serialize for a in items]
        i["Item"] = cat_items
    return jsonify(Category = sub_categories)
