from django.template.loader import get_template

from django.conf import settings

from django.utils.translation import gettext_lazy as _

from django.utils import translation

from mailjet_rest import Client
import os

class Mail:
    
    @staticmethod
    def send_complete_order(order, user):
        translation.activate(user.language)
        mailjet = Client(auth=(settings.MAILJET_PUB_KEY, settings.MAILJET_PRIV_KEY), version='v3.1')
        data = {
          'Messages': [
            {
              "From": {
                "Email": "orders@simplebuy.com",
                "Name": "SimpleBuy"
              },
              "To": [
                {
                  "Email": str(user.email),
                  "Name": str(user.username)
                }
              ],
              "Subject": str(_('Your SimpleBuy order #') + order.order_id),
              "TextPart": str(_('Important message')),
              "HTMLPart": str(get_template('orders/mails/complete.html')),
              "CustomID": "OrderEmail"
            }
          ]
        }
        result = mailjet.send.create(data=data)

        # print(result.status_code)
        # print(result.json())