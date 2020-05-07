from . import stripe

def create_card(user, token):
    source = stripe.Customer.create_source(
        user.customer_id,
        source=token
    )

    return source

def remove_card(card_id, user):
    response = stripe.Customer.delete_source(
        nested_id=card_id,
        id=user.customer_id
    )