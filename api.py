from flask import Flask
#from flask_oauth import OAuth
from flask import session, url_for, redirect, render_template, request, flash
import oauth2

app = Flask(__name__)


# Borrowed from Yelp oauth help files
# https://github.com/Yelp/yelp-api/tree/master/v2/python
#######################################


# following values unique to our group
consumer_key = '4EIHwPZt8DYZHqTXwm1A-Q'
consumer_secret = 'juXt69VHeOHgAKmpWt_OI5_6RDY'
token = 'r5k7SUhaEg_TIcsrhv4V4BLLW2e5z8gC'
token_secret = 'c3_YJgWWdCL6kNMD9ux7cFiJu9U'
# end of values

consumer = oauth2.Consumer(consumer_key, consumer_secret)


url = 'http://api.yelp.com/v2/search?term=bars&location=sf'
print 'URL: %s' % (url,)

oauth_request = oauth2.Request('GET', url, {})
oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
                      'oauth_timestamp': oauth2.generate_timestamp(),
                      'oauth_token': token,
                      'oauth_consumer_key': consumer_key})

token = oauth2.Token(token, token_secret)

oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)

signed_url = oauth_request.to_url()

print 'Signed URL: %s' % (signed_url,)

# End of borrowed code
###########################################


# if __name__=="__main__":
#     app.debug=True
#     app.run(host='0.0.0.0',port=5000)
