from flask import Flask,jsonify
from flask import request
from espn import EspnScrapper
app = Flask(__name__)


@app.route('/hello/', methods=['GET','POST'])
def welcome():
    username = request.args.get('username')
    password = request.args.get('password')
    domain = request.args.get('domain')
    if username is None or password is None or domain is None:
        response_dict = {
            "status_code": -1, "error_message": "Incorrect Api Usage. Entered value in one of the field is empty.", "success_message": ''
            }
    else:
        try:
            print(username, password, domain, sep= "\t")
            my_scraper_obj = EspnScrapper(username=username, password=password, domain=domain)
            response_dict = my_scraper_obj.main_loop()
        except Exception as _:
            import traceback
            traceback.print_exc()
            response_dict = {
                "status_code": -1, "error_message": "Incorrect Api Usage. Browser crashed server error.", "success_message": ''
                }
            print("We are in server exception")
    
    return jsonify(response_dict)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050)