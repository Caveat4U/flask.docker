# import newrelic 
# newrelic.agent.initialize()

from flask import Flask, request
import boto3
from pymongo import MongoClient

client = MongoClient()
app = Flask(__name__)

@app.route("/")
def hello():
   return "Hello World from Flask"

@app.route("/alert", methods=['GET', 'POST'])
def inbound_alert():
	"""
	Example alert opened policy
	{
	"created_at":"2014-03-04T14:41:07+00:00",
	"servers":["my.server.local"],
	"account_name":"Account name",
	"severity":"Critical",
	"message":"Disk IO > 85%",
	"short_description":"New alert on my.server.local",
	"long_description":"Alert opened: Disk IO > 85%",
	"alert_url":"http://PATH_TO_NEW_RELIC/accounts/nnn/incidents/nnn",
	"server_events":[{"server":"my.server.local","created_at":"2014-03-04T22:41:07Z","message":"Disk IO > 85%"}]
	}
	"""
	content = request.get_json(silent=True)
	server_name = content['servers'][0]
	db = client.alerts
	db.inbound_alert.insert_one(content)
	# Get the server that's having issues
	if "percona" in server_name:
		pass
	return "Nothing"

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True, port=2020)
