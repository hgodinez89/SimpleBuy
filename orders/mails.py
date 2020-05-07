from django.template.loader import get_template

from django.core.mail import EmailMultiAlternatives

from django.conf import settings

from django.urls import reverse

from django.utils.translation import gettext_lazy as _

from django.utils import translation

class Mail:

    @staticmethod
    def get_absolute_url(url):
        if settings.DEBUG:
            return 'http://127.0.0.1:8000{}'.format(
                reverse(url)
            )
    
    @staticmethod
    def send_complete_order(order, user):
        translation.activate(user.language)
        subject = _('Your SimpleBuy order #') + order.order_id
        template = get_template('orders/mails/complete.html')
        content = template.render({
            'user': user,
            'next_url': Mail.get_absolute_url('orders:completeds')
        })

        message = EmailMultiAlternatives(subject, 
                                         _('Important message'), 
                                         settings.EMAIL_HOST_USER,
                                         [user.email])
        
        message.attach_alternative(content, 'text/html')
        message.send()