import translators
from dataclasses import dataclass

@dataclass
class TranslateResult:
    # provider: 



def translate(input_text):
    translate_list = ['google', 'bing', 'baidu', 'youdao']
    result_list = list()
    for site in translate_list:
        result = getattr(translators, site)(input_text, 'auto', 'en')
        print(result)


