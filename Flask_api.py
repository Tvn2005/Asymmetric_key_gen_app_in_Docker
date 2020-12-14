# Using flask to make an api 
# import necessary libraries and functions 
from flask import Flask, jsonify, request,render_template
#from waitress import serve

# creating a Flask app 
app = Flask(__name__) 

# on the terminal type: curl http://127.0.0.1:5000/ 
# returns hello world when we use GET. 
# returns the data that we send when we use POST. 
@app.route('/', methods = ['GET', 'POST']) 
def home(): 
	if(request.method == 'GET'): 

		data = "Get the private and public keys "
    #return render_template('get_keys.html', form=form)
		return render_template('get_keys.html')#return jsonify({'data': data}) 


@app.route('/key',methods= ['GET'])
def Rsakeys():
    #Importing necessary modules
    from Crypto.Cipher import PKCS1_OAEP
    from Crypto.PublicKey import RSA
    from binascii import hexlify

    #The message to be encrypted
    #message = b'Public and Private keys encryption'

    #Generating private key (RsaKey object) of key length of 1024 bits
    private_key = RSA.generate(1024)

    #Generating the public key (RsaKey object) from the private key
    public_key = private_key.publickey()
    #print(type(private_key), type(public_key))
    #print((private_key), (public_key))
    
    private_pem = private_key.exportKey('PEM').decode()
    public_pem = public_key.exportKey('PEM').decode()
    #print(type(private_pem), type(public_pem))
    #print((private_pem), (public_pem))
    
    return jsonify({'Private key': private_pem,
                   'Public key': public_pem}) 

# driver function 
if __name__ == '__main__': 

	app.run(debug=True, use_reloader=False)
  #serve(app, host="0.0.0.0", port=8080)
  