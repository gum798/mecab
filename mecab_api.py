import MeCab
from flask import Flask
from flask_restful import Resource, Api
# from flask_restful import reqparse
from flask import request
# from concurrent.futures import ThreadPoolExecutor
# from threading import Thread


app = Flask(__name__)
api = Api(app)


def get_part_of_speech(feature):
    # return '-'.join([v for v in feature.split(',')[:4] if v != '*'])
    # feature = feature.split('Inflect,')[len(feature.split('Inflect,'))-1]
    # return feature.split(',')[0].split('+')[0]
    return feature.split(',')[0]

def get_part_of_speech2(feature):
    # return '-'.join([v for v in feature.split(',')[:4] if v != '*'])
    # feature = feature.split('Inflect,')[len(feature.split('Inflect,'))-1]
    # return feature.split(',')[0].split('+')[0]
    return feature.split(',')[0].split('+')

def get_reading(feature):
    return feature.split(',')[7]

def get_reading2(feature):
    a = feature.split(',')[7].split('+')
    b = []
    i = 0
    while i < len(a):
        b.append(a[i].split('/')[0])
        i+=1
    return b

def get_base_form(feature):
    return feature.split(',')[6]

def check_inflect(feature):
    return feature.split(',')[4] == 'Inflect'


class Mecab(Resource):


    def post(self):
        try:
            # parser = reqparse.RequestParser()
            # parser.add_argument('sentence', type=str)
            # args = parser.parse_args()

            # _userSentence = args['sentence']

            _userSentence = request.json.get('sentence')
            print(_userSentence)

            m = MeCab.Tagger('-d /opt/syntax/mecab-ko-dic-2.1.1-20180720')
            # m = MeCab.Tagger()
            ret = m.parse(_userSentence)
            ret1 = m.parseToNode(_userSentence)
            print(ret)

            tokens = []
            while ret1:
                    feature = ret1.feature + ',*,*'

                    part_of_speech = get_part_of_speech2(feature)
                    # reading = get_reading(feature)
                    # base_form = get_base_form(feature)
                    surface = []
                    if check_inflect(feature):
                        surface = get_reading2(feature)
                    else:
                        surface.append(ret1.surface)
                    i = 0
                    while i < len(part_of_speech):
                        token = {
                            "surface": surface[i],
                            # "feature": ret1.feature,
                            "pos": part_of_speech[i],
                            # "reading": reading,
                            # "baseform": base_form,
                            # "stat": ret1.stat,
                        }
                        if part_of_speech[i] not in 'BOS/EOS':
                            tokens.append(token)
                        i +=1
                    ret1 = ret1.next

            print(tokens)

            # return {'result': ret}
            return tokens
            # return {'result': _userSentence}
            # return {'result': args}
        except Exception as e:
            return {'error': str(e)}

api.add_resource(Mecab, '/mecab')

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5001, debug=False)
	# kwargs = {'host': '0.0.0.0', 'port': 5001, 'threaded': True, 'use_reloader': False, 'debug': False}
	# flaskThread = Thread(target=app.run, daemon=True, kwargs=kwargs).start()
    # srv = ThreadedWebsocketServer("0.0.0.0", 5000, app)
    # srv.serve_forever()

