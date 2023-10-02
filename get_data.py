import requests

cookies = {
    '_zap': '767b090e-7f57-4691-afde-19b1fdc249db',
    'd_c0': 'ACATd3gUqxaPTkhTbe8Qz_xJ6bNHlvDnQdc=|1682218104',
    'YD00517437729195%3AWM_TID': 'Ee%2BU0xWZXBtFVRBUUReUb54fEbEW1Tfq',
    'YD00517437729195%3AWM_NI': 'aQjMJgiYVvDIHehXOuIYckyImgNR8QQQkUCsn8%2B11HscbAqOLfNfWgg62MTb%2BEXdq8pPlwlIaqsq9GDQSPyyjuV6c9PrjzpyKq7cjo2JLy6f%2BopopOesVoB%2FVUi7wbxPVmE%3D',
    'YD00517437729195%3AWM_NIKE': '9ca17ae2e6ffcda170e2e6ee86aa48889b8697d26af4ef8fa3c45b869f8f83c861aeef828aef5e919c9f88cb2af0fea7c3b92aa38fa6aec96dab879a97c7438cbba8b9ce7f8b87ad8cfc43afb982b3bb5b938fa5b6c279aee8e5d2b444b1bdaea2f44590ba8287d66da5eafeaed76ae99b9885f434b490a498ef43a3afbd92bc4d888f9db1fc73aaab9ad7e23394aea69bf37389aff984e965f296849ab56ee9b1c090f345a7ad9a90c125968ba7d8f66abc909a8ec837e2a3',
    'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49': '1688892941,1689035687,1689577851,1691032543',
    '_xsrf': 'f1f4a62b-abe2-49f0-8fe6-45460f507f34',
    'KLBRSID': 'fe0fceb358d671fa6cc33898c8c48b48|1696222386|1696222375',
}

headers = {
    'authority': 'www.zhihu.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'cookie': '_zap=767b090e-7f57-4691-afde-19b1fdc249db; d_c0=ACATd3gUqxaPTkhTbe8Qz_xJ6bNHlvDnQdc=|1682218104; YD00517437729195%3AWM_TID=Ee%2BU0xWZXBtFVRBUUReUb54fEbEW1Tfq; YD00517437729195%3AWM_NI=aQjMJgiYVvDIHehXOuIYckyImgNR8QQQkUCsn8%2B11HscbAqOLfNfWgg62MTb%2BEXdq8pPlwlIaqsq9GDQSPyyjuV6c9PrjzpyKq7cjo2JLy6f%2BopopOesVoB%2FVUi7wbxPVmE%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee86aa48889b8697d26af4ef8fa3c45b869f8f83c861aeef828aef5e919c9f88cb2af0fea7c3b92aa38fa6aec96dab879a97c7438cbba8b9ce7f8b87ad8cfc43afb982b3bb5b938fa5b6c279aee8e5d2b444b1bdaea2f44590ba8287d66da5eafeaed76ae99b9885f434b490a498ef43a3afbd92bc4d888f9db1fc73aaab9ad7e23394aea69bf37389aff984e965f296849ab56ee9b1c090f345a7ad9a90c125968ba7d8f66abc909a8ec837e2a3; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1688892941,1689035687,1689577851,1691032543; _xsrf=f1f4a62b-abe2-49f0-8fe6-45460f507f34; KLBRSID=fe0fceb358d671fa6cc33898c8c48b48|1696222386|1696222375',
    'referer': 'https://www.zhihu.com/question/589682298/answer/3223847748?utm_id=0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/117.0.0.0',
    'x-ab-param': '',
    'x-requested-with': 'fetch',
    'x-zse-93': '101_3_3.0',
    'x-zse-96': '2.0_MCiF/l1/+Vf1sj=zfe9eY0D+0D7JJ3C8171/fLkBZdRvVqx5s5rO=ge0moMp6nJd',
}

response = requests.get(
    'https://www.zhihu.com/api/v4/answers/3223847748/related-readings?include=data%5B*%5D.is_normal%2Ccomment_count%2Cvoteup_count%3Bdata%5B%3F%28type%3Dlive%29%5D.seats%3Bdata%5B%3F%28type%3Dremix_album%29%5D.description&support_sdk=1&utm_source=baidu',
    cookies=cookies,
    headers=headers,
)
