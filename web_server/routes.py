import json
from datetime import datetime
from flask import jsonify, flash, redirect, request, abort, Response
from web_server import app
from .database import insert_transaction, spend_points, view_balance

# API Routes
@app.route("/api/user/balance", methods=['GET'])
def check_balance():
  
    balances = view_balance()
    balances_json = json.dumps(balances)
    return balances_json

@app.route("/api/user/transaction", methods=['PUT'])
def add_transaction():
    form = request.json
    payer = str(form['payer'])
    points = int(form['points'])
    timestamp = str(form['timestamp'])

    insert_transaction(payer, points, timestamp)
    return Response('{"message":"Transaction Added!"}', status=202)


@app.route("/api/user/redeem", methods=['PUT'])
def redeem_points():
    form = request.json
    points = int(form['points'])
    usage = spend_points(points)
    now = datetime.now()
    today = now.strftime("%Y-%d-%mT%H:%M:%SZ")
    for payer, points in usage.items():
        insert_transaction(payer, points, today)
    usage_json = json.dumps(usage)
    return '[' + usage_json + ']'


