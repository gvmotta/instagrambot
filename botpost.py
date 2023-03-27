from instagrapi import Client
from instagrapi.types import Usertag, Location
from pyChatGPT import ChatGPT

nome = str(input("Digite o nome do tênis: "))
session_token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..DsLDn4KLRgGhqL_l.cmXpHL4AZZ-PN3viEcM_V9zfgYM4DiPtSoiw3pdCOSse9lqj4b5_wsLR8CNfhai3tGLjF6cv7xexBnV00lvUCnfvvRftQqiYUQrIxaq1kifGQmaKVvEK53FwdrQnDfi3I8AP-GvPancXsiMx1w3y4Cw8_F3oI9ofNt49mVIPB3sdMkwzwwza86ceqMUE0xDWFDdCmetBtugxGw1BHl-GcxmD5iK5n6oEV4VXId7XylKOJQ_ejqAtUAOmrS5TQb_FIWP_CvoaFUGVRA7u9veaxT_cl3v0mLF0IQKksgYtB8QZ3YqE6FCggZ4muNkZaqkCRTyJ9q2GJ3IoIPN2jDrsI3ugK2QIVsunV35royAyyCsOo2lxtx96vj1vcDKw9fgfdauswEXPa_OMq7lAd3cuk6e-IwEiJXcTvzEWK-XnRhzKKf0DrSr_RFZdA_Mx_X7XMykSvMKXBatAQb1OHuFJxmc8zS4TTl0KlbsGDgm5z2qZYMmQ3Ie7DSTKvSZzH1GgOk9dzguEDtKPDddeb3ubRj6sd7cazl7DSoM_pFgjYbNpxgQOk8ru7Q5M5Ja596LpA57fG-CD9T_BFbG4C4eNHlCkqIQDxtJX7IcLVPbHajukkXStWrTg098K17yAolExl_QqRkBSNlEuY33Qc3RQXh72S8RsKeKEQwUX87f1iOHEtpn-1ySY7lByJQwpfLSkg-89fNYRrV9yWcJk8iHvmSR7c0I1V3tqzdt1Lub5uXxARhPYBKjnAyYqiQYUASqOX7jA8ZgxYFhdWOYlz4dz-gkYI9FB0icFWTWJO4zbVyVIeGmI-Am6MmtFpzQvvu7UCSzc3Hvl7oMpcPUGSQ_LH03h9ouUrCuIZluyY9zeLQtX4mv0JlWxpvO3oFgCoWCpjtB5fFzJ9Wo5ERFDe0k9qTfU0d1-xjt8MvLrZp61XjBkg9yyXHpQHkUwDF5NL-TKAfyeKha_SUnXSQ4z7QOWkQmHH-LXTTh7H2nfYwQk3jRZOZgrCt1kdXTC7WgU0MBm_OqcRhnSybTiEBDXSgyLDf0FfnG88e8001-sa2g_E-4hL2zOZVUrcS_gY9ChKXUNrKV-LVUm6zlb05yXtopWUnXBGF1kiDKEUqodmVknAP5TOkzapRcUfY4vnSYrYl57cMWFfdjf1pVc1hIfG3PXhvqiZJtt0p5-qvfBUNBOkculgTGMchFnq1F_SF9qHjNpmbiRObcNbUjtalIYnE1GEF-eRq016-0IgcnEvV64xMsiPCXbataP8cQHei5lCXHIzwYuVeU7cJR4ZC3P1gXHLHB1Rm0AEPWQby2Jela61KlWR5xudbhq1L1eDsPh5o2KPjfSGtvBJ1GTfZ4nMnxJ-a_hhajuloVZFXdvM2m829gztmetGOZPMooZivCyhYKauaQwsQq9hM8o0YS36WEB3D7iihK3okY_9bZHs_puC2hSm4kGDzRu-buXkWC0AETHZFeZicKydqw-pTijknuWStkSRKxg-BTA1kYFB1he-Nreuinwhg0c-bmUuf6HtqG8LgEnlotRFKgLwUsXvR5Ic2fXyfl3umZboeDTSYqhBlRLg-v24_42VvEig7cvATLyqLz0Ta_nuYb-V4RQXWEzdohxA1K2JEd7m_3eLjp4BfVrFRFDUxV9H-a-pODrKrfujDC2ldS7Wv3RrrS8WlEFwxjM5LUxcI9yD45VfSV1c7SZr85Yd3Ao8eFJAzqaUsa1O1Y5d7AZ_iqKLaYJgmcY7guLrtrtbshW5tYwwaNJSl11yk5bVway6M8pfwscCrav5u-8ljZgBPUJ9g1Vn28lTQ22CGQjS24IhpMrNJJf8VjuC5Nxk4fw9QNGbpzELPaPMufeIyYdc05Es33RcpWz0iplBmowIAnNzgABbrJpP-vNb7_aSGhc54TL1QNCZ7TdhiUEUqng4zGNlDBrpvoEVR3zBXrwNn0S1yvDGEeaP3nF_M_UutXrs_U4HhoFCNkjOxSHsHw9oSs2wpvZEQcVW5DwzIbHIeOUzFdz2UE4w255VSDgUcPI1CNHVViJPkkvJ4xtDw9xm9BY8H0R6J0lSUL2zcELXx3ri-xvCT5ZjmPBTeYL-SXC-7iXEt0KKyZNN6Fg4VKmga588isQwk9t-NQyatcPxng0A-KBiGFK6PblLnEoXBE0hq2zDZ8BCJI_Rb_QrraMg1hAH5TOejxyZN-KFV2aprwC4R3z0v7CvDzF0KCDIXoRxpnp5_MYb9eZYK5ViGxM_VchYXm4xJGOvQbZZ0b0DbMtu9YYzwm2NUrNzzmx0fTp9L5zBQeQvMEKM1dUEWmF49GYI7HTw9hVKT-waGAJQWQncQ2Ed9mUNY5Wo0P34KtNbGAETXUaVbl7I5hdr0wkapCVhfPaz31i56clsCmhassziLaEf-JUzpU2_14KOyLQ0e3z3mgw1YH1MVL_AiAEI2AjzhH1sQ43nKKabwLVCZjitmDH-OWwwQ698wHwhW5Oj5tQuvdp1DKcCYz8XO7z7cn2j8YHm7KOT5_oxDhMbtTUMV1HATvZBtJBAMe-Ag.Cx06eLXozJZF5GO0XMQyow"
api = ChatGPT(session_token)

resp = api.send_message('Seja um ótimo vendedor e faça uma descrição que me convença a comprar o tênis {} começando a frase falando "O tênis" em um texto de um parágrafo de 3 linhas sem falar da sua sola de EVA'.format(nome))

# Encontra o índice da primeira ocorrência da palavra "tênis"
indice = resp['message'].find('O tênis')

# Faz slicing da string a partir do índice encontrado
parte_tenis = resp['message'][indice:].rstrip()

hashtags = "\n\n#sneakers #dunk #nike #airjordan #store #tenis"

resp1 = "{}\n- Fotos Reais do produto\n- Chama direct para mais detalhes\n".format(nome) + parte_tenis + hashtags

print(resp1)

cl = Client()
cl.login("splashsneakers.inc", "LUCIANe101@#")

List = [r"C:\Users\gusta\OneDrive\Imagens\app\fotosparapostar\1.jpg", r"C:\Users\gusta\OneDrive\Imagens\app\fotosparapostar\2.jpg", r"C:\Users\gusta\OneDrive\Imagens\app\fotosparapostar\3.jpg"]
List2 = [r"C:\Users\gusta\OneDrive\Imagens\app\fotosparapostar\4.jpg", r"C:\Users\gusta\OneDrive\Imagens\app\fotosparapostar\5.jpg", r"C:\Users\gusta\OneDrive\Imagens\app\fotosparapostar\6.jpg"]
List3 = [r"C:\Users\gusta\OneDrive\Imagens\app\fotosparapostar\7.jpg", r"C:\Users\gusta\OneDrive\Imagens\app\fotosparapostar\8.jpg", r"C:\Users\gusta\OneDrive\Imagens\app\fotosparapostar\9.jpg"]

media = cl.album_upload(
    paths=List,
    caption=resp,
    extra_data={
        "custom_accessibility_caption": "",
        "like_and_view_counts_disabled": 1,
        "disable_comments": 0,
    }
)
media = cl.album_upload(
    paths=List2,
    caption=resp,
    extra_data={
        "custom_accessibility_caption": "",
        "like_and_view_counts_disabled": 1,
        "disable_comments": 0,
    }
)
media = cl.album_upload(
    paths=List3,
    caption=resp,
    extra_data={
        "custom_accessibility_caption": "",
        "like_and_view_counts_disabled": 1,
        "disable_comments": 0,
    }
)