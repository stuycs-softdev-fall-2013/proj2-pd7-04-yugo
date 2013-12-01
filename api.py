from flask import Flask
#from flask_oauth import OAuth
from flask import session, url_for, redirect, render_template, request, flash
import urllib2
import oauth2
import json

app = Flask(__name__)


#address is a string in the form of {street address, neighborhood, city, state}
#service is a string
###All ' ' must be instead '+'
def yelpAPI(address,service,limit):

    ##########################################################
    # Borrowed from Yelp oauth help files                    #
    # https://github.com/Yelp/yelp-api/tree/master/v2/python #
    ##########################################################
    

    # following values unique to our group ############
    consumer_key = '4EIHwPZt8DYZHqTXwm1A-Q'           #
    consumer_secret = 'juXt69VHeOHgAKmpWt_OI5_6RDY'   #
    token = 'r5k7SUhaEg_TIcsrhv4V4BLLW2e5z8gC'        #
    token_secret = 'c3_YJgWWdCL6kNMD9ux7cFiJu9U'      #
    # end of values ###################################
    
    consumer = oauth2.Consumer(consumer_key, consumer_secret)


    ### following code customized by our group


    #limit = 1; #number of results returned

    url = 'http://api.yelp.com/v2/search?term=%s&location=%s&limit=%d&format=json'%(service, address, limit)


    ### end of customized code 
    

    #print 'URL: %s' % (url,)


    oauth_request = oauth2.Request('GET', url, {})
    oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
                          'oauth_timestamp': oauth2.generate_timestamp(),
                          'oauth_token': token,
                          'oauth_consumer_key': consumer_key})

    token = oauth2.Token(token, token_secret)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()
    
    #print 'Signed URL: %s' % (signed_url,)
    
    ############################
    # End of borrowed code     #
    ############################
    
    return signed_url


def testURL(url):
    connection = urllib2.urlopen(url)
    response = json.load(connection)
    connection.close()
    return response


#returns list of dicts
#each dict has keys
#'name' = <name of place>
#'address' = <(string) address of place>
def getNameAddress(service, curAddress, numOfReturnedBusinesses):
    url = yelpAPI(curAddress, service, numOfReturnedBusinesses)
    response = testURL(url)

    buses = response["businesses"]
    businesses = []
    
    i = 0
    for elem in buses:
        addressList = response["businesses"][i]["location"]["display_address"]
        addr = str(addressList[0] + " " + addressList[2] + " " + addressList[3])

        busDict = {}
        busDict["address"] = addr
        busDict["name"] = response["businesses"][i]["name"]

        businesses.append(busDict)
        i = i + 1

    return businesses
        
    
print getNameAddress("cafe", "215 West 88th St New York, NY", 3)  

#if __name__=="__main__":
#     app.debug=True
#     app.run(host='0.0.0.0',port=5000)
    
