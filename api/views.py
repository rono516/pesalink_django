from django.http import JsonResponse
import requests
from django.shortcuts import render
client_id = "65ddb2bd197476634ded6d82ed5ed7fd"
client_secret = "870f83bcd5a17167c0f642000e8c4346"
token_url = "https://api.connect.stanbicbank.co.ke/api/sandbox/auth/oauth2/token"
scope = "payments"

def index(request):
    return render(request, "api/index.html")
def auth_token(request):
    payload = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': scope
    }
    response = requests.post(token_url,data=payload)
    return JsonResponse(response.json())

# def make_payment(request):
#     access_token = "AAIgNjVkZGIyYmQxOTc0NzY2MzRkZWQ2ZDgyZWQ1ZWQ3ZmROEIO1ym2AbDSCoavLrdBbSX4FUDF4mymJU5l2tdW1AvNwg2aYiiT5gyiVOGnbuZf0vZTPMQNROPT_lyKTuX9TBEVqTUvov-SWcXfvmGOqyAlqtK6jsvox4W2kbQU_fjo"
#     url = "https://api.connect.stanbicbank.co.ke/api/sandbox/pesalink-payments/"

#     payload = {
#     "originatorAccount": {
#         "identification": {
#         "mobileNumber": "254737696956"
#         }
#     },
#     "requestedExecutionDate": "2021-10-27",
#     "sendMoneyTo": "ACCOUNT.NUMBER",
#     "dbsReferenceId": "98989271771176942",
#     "txnNarrative": "TESTPESALINK",
#     "callBackUrl": "https://clientdomain.com/client/Callback",
#     "transferTransactionInformation": {
#         "instructedAmount": {
#         "amount": "500",
#         "currencyCode": "KES"
#         },
#         "counterpartyAccount": {
#         "identification": {
#             "recipientMobileNo": "25472XXXXXXXX",
#             "recipientBankAcctNo": "01008747142",
#             "recipientBankCode": "07000"
#         }
#         },
#         "counterparty": {
#         "name": "HEZBON",
#         "postalAddress": {
#             "addressLine": "KENYA",
#             "postCode": "1100 ZZ",
#             "town": "Nairobi",
#             "country": "KE"
#         }
#         },
#         "remittanceInformation": {
#         "type": "FEES PAYMENTS",
#         "content": "SALARY"
#         },
#         "endToEndIdentification": "5e1a3da132cc"
#     }
#     }
#     headers = {
#         "Authorization": f"Bearer {access_token}",
#         "content-type": "application/json",
#         "accept": "application/json"
#     }

#     response = requests.post(url, data=payload, headers=headers)
#     return JsonResponse(response.json())


#     # print(response.text)
# ss


def make_payment(request):
    access_token = ""
    url = "https://api.connect.stanbicbank.co.ke/api/sandbox/pesalink-payments/"

    payload = {
        "originatorAccount": {
            "identification": {
                "mobileNumber": "254737696956"
            }
        },
        "requestedExecutionDate": "2021-10-27",
        "sendMoneyTo": "ACCOUNT.NUMBER",
        "dbsReferenceId": "98989271771176942",
        "txnNarrative": "TESTPESALINK",
        "callBackUrl": "https://clientdomain.com/client/Callback",
        "transferTransactionInformation": {
            "instructedAmount": {
                "amount": "500",
                "currencyCode": "KES"
            },
            "counterpartyAccount": {
                "identification": {
                    "recipientMobileNo": "25472XXXXXXXX",
                    "recipientBankAcctNo": "01008747142",
                    "recipientBankCode": "07000"
                }
            },
            "counterparty": {
                "name": "HEZBON",
                "postalAddress": {
                    "addressLine": "KENYA",
                    "postCode": "1100 ZZ",
                    "town": "Nairobi",
                    "country": "KE"
                }
            },
            "remittanceInformation": {
                "type": "FEES PAYMENTS",
                "content": "SALARY"
            },
            "endToEndIdentification": "5e1a3da132cc"
        }
    }
    headers = {
        "Authorization": f"Bearer {access_token}",
        "content-type": "application/json",
        "accept": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    return JsonResponse(response.json())

    # print(response.text)

# {
#   "originatorAccount": {
#     "identification": {
#       "mobileNumber": "254737696956"
#     }
#   },
#   "requestedExecutionDate": "2021-10-27",
#   "sendMoneyTo": "ACCOUNT.NUMBER",
#   "dbsReferenceId": "98989271771176942",
#   "txnNarrative": "TESTPESALINK",
#   "callBackUrl": "https://clientdomain.com/client/Callback",
#   "transferTransactionInformation": {
#     "instructedAmount": {
#       "amount": "500",
#       "currencyCode": "KES"
#     },
#     "counterpartyAccount": {
#       "identification": {
#         "recipientMobileNo": "254792009556",
#         "recipientBankAcctNo": "01008747142",
#         "recipientBankCode": "07000"
#       }
#     },
#     "counterparty": {
#       "name": "HEZBON",
#       "postalAddress": {
#         "addressLine": "KENYA",
#         "postCode": "1100 ZZ",
#         "town": "Nairobi",
#         "country": "KE"
#       }
#     },
#     "remittanceInformation": {
#       "type": "FEES PAYMENTS",
#       "content": "SALARY"
#     },
#     "endToEndIdentification": "5e1a3da132cc"
#   }
# }

# ss