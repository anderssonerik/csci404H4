import twitter
publicKey = 'Dhp3ub7leb4Pby1Dyv2PeCzCN'
secretKey = 'sLMqzuWVEGyd3juuVE9sfU6LihFu3zL8hCPnY57lGQv8OLdDRU'
accessToken = '40372113-3D0Lrju8zptFZiQiNNe9sCeGykZSQFjixYJEe8SST'
accessTokenSecret = 'Cv3dB34pGOAIQeNf162cq6pdXP64dYlLobGDOLu7Fk9HB'
api = twitter.Api(consumer_key=publicKey,
				  consumer_secret=secretKey,
				  access_token_key=accessToken,
				  access_token_secret=accessTokenSecret)

print(api.VerifyCredentials())