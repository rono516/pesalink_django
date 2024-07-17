from django.http import JsonResponse
import requests
from django.shortcuts import render
client_id = "31ed5023ca172de01eb8fdd71c3f54b2"
client_secret = "4193aac9e0ac9afd300ac4c40f2b4b29"
token_url = "https://api.connect.stanbicbank.co.ke/api/sandbox/auth/oauth2/token"
scope = "payments"

# KBS Accounts
# 01040304011
# 20040304211
# 20040304411
# Member ID - 40304
# Member ID - 29999
# 0102999911
# 20029999211
# 2002999211
# 20029999411

# Test Kba Credentials
# 65ddb2bd197476634ded6d82ed5ed7fd key
# 870f83bcd5a17167c0f642000e8c4346 secret

# Test kba 2 Credentials
# aa4f56e3ac57c12d9907802e9406570e key
# 18c282236b27115e764f58ede7d1f8ae secret

# Test kba 3 Credentials
# 2003a03718f42899392cd70794570af5  key
# 94893dae61ebaa23c2ca7525f4ac8fa3  secret

# Test kba 4 Credentials
# 469e3b6fb0736e55559904d2dd97863c  key
# 42ef060b0fd2217921e6845b389ec3c0  secret

# Test kba 5 Credentials
# 2002999211
# 7b3be122421b39bc2f5970d2e582fef4  key
# b031174410b52529900f88d6bd5d4849  secret

# test kba 6 Credentials
# 20029999211 - account number
# 31ed5023ca172de01eb8fdd71c3f54b2 key
# 4193aac9e0ac9afd300ac4c40f2b4b29 secret
def index(request):
  return render(request, "api/index.html")
def sendtophone(request):
  return render(request, "api/sendtophone.html")
def sendtoaccount(request):
  return render(request, "api/sendtoaccount.html")

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
    access_token = "AAIgMzFlZDUwMjNjYTE3MmRlMDFlYjhmZGQ3MWMzZjU0YjK2gFqhCxbNSfKDyz9tbMmCkrJelGoX38z1n_RuxTBEbm1qJgtooYeGe0v-YIOillSYbKadEOuPLx4WQWDyGH9iwYWfAmEGQRkz7nD2NIWyNPQ-vkB1Tbm-WNK39eSwLQA"
    url = "https://api.connect.stanbicbank.co.ke/api/sandbox/pesalink-payments/"

    payload = {
        "originatorAccount": {
            "identification": {
                # "mobileNumber": "254737696956"
                "mobileNumber": "254721615262"
            }
        },
        "requestedExecutionDate": "2021-10-27",
        "sendMoneyTo": "ACCOUNT.NUMBER",
        "dbsReferenceId": "98989271771176942",
        "txnNarrative": "TESTPESALINK",
        "callBackUrl": "https://clientdomain.com/client/Callback",
        "transferTransactionInformation": {
            "instructedAmount": {
                "amount": "10",
                "currencyCode": "KES"
            },
            "counterpartyAccount": {
                "identification": {
                    # "recipientMobileNo": "254721615262",
                    # "recipientBankAcctNo": "01008747142",
                    "recipientBankAcctNo": "0102999911",
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

schema = {
  "type": "object",
  "description": "A Resftful(JSON) Payload request with the details required to initiate a pesalink payment. Instant payments are currently supported",
  "required": [
    "requestedExecutionDate",
    "txnNarrative",
    "dbsReferenceId",
    "transferTransactionInformation",
    "originatorAccount"
  ],
  "properties": {
    "originatorAccount": {
      "type": "object",
      "properties": {
        "identification": {
          "type": "object",
          "properties": {
            "mobileNumber": {
              "type": "string",
              "example": "254737696956"
            }
          }
        }
      }
    },
    "requestedExecutionDate": {
      "type": "string",
      "example": "2021-10-27",
      "description": "The current system date (EAT) in the format YYYY-MM-DD"
    },
    "sendMoneyTo": {
      "type": "string",
      "enum": [
        "ACCOUNT.NUMBER"
      ],
      "description": "When sending to Account Number use ACCOUNT.NUMBER",
      "example": "ACCOUNT.NUMBER"
    },
    "dbsReferenceId": {
      "type": "string",
      "example": "98989271771176942",
      "description": "This is 3rd party system unique reference. Our systems will use this reference to track your transactions."
    },
    "txnNarrative": {
      "type": "string",
      "example": "TESTPESALINK"
    },
    "callBackUrl": {
      "type": "string",
      "example": "https://clientdomain.com/client/Callback",
      "description": "Future use"
    },
    "transferTransactionInformation": {
      "type": "object",
      "properties": {
        "instructedAmount": {
          "type": "object",
          "properties": {
            "amount": {
              "type": "string",
              "example": "500"
            },
            "currencyCode": {
              "type": "string",
              "example": "KES"
            }
          }
        },
        "counterpartyAccount": {
          "type": "object",
          "properties": {
            "identification": {
              "type": "object",
              "properties": {
                "recipientMobileNo": {
                  "type": "string",
                  "example": "25472XXXXXXXX",
                  "description": "When the Mobile Number is populated, The account Number should be left blank"
                },
                "recipientBankAcctNo": {
                  "type": "string",
                  "example": "01008747142",
                  "description": "When account Number is populated"
                },
                "recipientBankCode": {
                  "type": "string",
                  "example": "07000"
                }
              }
            }
          }
        },
        "counterparty": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "example": "HEZBON"
            },
            "postalAddress": {
              "type": "object",
              "properties": {
                "addressLine": {
                  "type": "string",
                  "example": "KENYA"
                },
                "postCode": {
                  "type": "string",
                  "example": "1100 ZZ"
                },
                "town": {
                  "type": "string",
                  "example": "Nairobi"
                },
                "country": {
                  "type": "string",
                  "example": "KE"
                }
              }
            }
          }
        },
        "remittanceInformation": {
          "type": "object",
          "properties": {
            "type": {
              "type": "string",
              "example": "FEES PAYMENTS"
            },
            "content": {
              "type": "string",
              "example": "SALARY"
            }
          }
        },
        "endToEndIdentification": {
          "type": "string",
          "example": "5e1a3da132cc"
        }
      }
    }
  }
}