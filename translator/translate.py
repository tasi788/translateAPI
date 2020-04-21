import translators
import pydeepl


class Translate:
    def __init__(self):
        self.result_list = list()

    def gooyou(self, input_text):
        # bing, google, youdao, deepl
        translate_list = ['google', 'youdao']
        for site in translate_list:
            result = getattr(translators, site)(
                input_text, 'auto', 'en', if_use_cn_host=False)
            tmp = {'provider': site.capitalize(), 'status': True,
                   'result': result}
            self.result_list.append(tmp)

    def bing(self, input_text):
        result = bing_tr(input_text, to_lang='en')
        tmp = {'provider': 'Bing', 'status': True, 'result': result}
        self.result_list.append(tmp)

    def deepl(self, input_text):
        result = pydeepl.translate(input_text, 'EN')
        tmp = {'provider': 'DeepL', 'status': True, 'result': result}
        self.result_list.append(tmp)
