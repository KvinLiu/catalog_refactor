# Item Catalog Application
This is a item catalog application, backend implemented by Flask. front-end implemented by Bulma.

## How it work
1. `cd` into the project folder
2. type `python application.py` command
3. You will get nothing for the first time, only beacuse the database was empty
4. type `python exampleitems.py` for create some example data.
5. Now reopen the app It will look better

## Basic route
For server-side several routes routes were created.
1. `/login` for google account login.
2. `/gconnect` for server exchange security info with google server.
3. `/disconnect` for user logout
these three routes only reply **GET** mehtod

4. `/` show all items
5. `/catalog/<int:item_cat>/<item_name>` show individual item
6. `/catalog/<category_id> /catalog/<category_id>/items` show categories
these routes also only reply **GET** method

7. `/catalog/new` create item
8. `/catalog/<item>/edit` edit item
9. `/catalog/<item>/delete` delete item
these routes reply both **GET** and **POST** method

## API endpoint
Get catalog info with JSON format by visiting `/catalog.json` route.

## Project env
All project env requiements in `requirements.txt`, install by
`pip install -r requirements.txt`.

