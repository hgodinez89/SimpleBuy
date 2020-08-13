<p align="center">

  <h3 align="center">SimpleBuy</h3>

  <p align="center">
    This is an E-commerce website.
    <br>
    <a href="https://github.com/hgodinez89/SimpleBuy/issues/new" target="_blank">Report bug</a>
  </p>
</p>


## What’s In This Document
- [What’s In This Document](#whats-in-this-document)
- [What is this?](#what-is-this)
- [Version History](#version-history)
- [Preview](#preview)
- [Try a demo](#try-a-demo)
- [Have questions?](#have-questions)
- [Thanks](#thanks)

## What is this?

This is an E-commerce website integrated with Stripe platform, this integration allows online payment processing and storing with all security measures. It was created with Django, HTML, CSS (TailwindCSS), JavaScript & MySQL Database.</br>
Important if you want to try this website in your computer, you need to create your own **secret.py** file (I recommend you create it in the store folder, next to settings.py), it should has a format similar like this: </br> </br>
```
class Secrets:
    SECRET_KEY_DJANGO = 'your own Django's apiKey, it's generated when your start your project'
    STRIPE_PUB_KEY = 'your own public Stripe's apiKey'
    STRIPE_PRIV_KEY = 'your own private Stripe's apiKey'
    HOST_DB = 'your own host database'
    USER_DB = 'you database user'
    PASSWORD_DB = 'user's database password'
    NAME_DB = 'database name'
    MAILJET_PUB_KEY = 'your own public MailJet's apiKey to send notifications from GCP for customers orders, etc'
    MAILJET_PRIV_KEY = 'your own private MailJet's apiKey to send notifications from GCP for customers orders, etc'
```
</br></br>
Thanks for your visit! 👍

## Version History

| Version |       Date         |             Comments             |
| ------- | ------------------ | -------------------------------- |
| 1.0     | October 2019       | Initial release                  |

## Preview

<img src="https://res.cloudinary.com/developerteam/image/upload/v1588770815/SimpleBuy/home.png" alt="EnglishHome">
</br>
<img src="https://res.cloudinary.com/developerteam/image/upload/v1588771073/SimpleBuy/signin.png" alt="SignIn">
</br>
<img src="https://res.cloudinary.com/developerteam/image/upload/v1588771210/SimpleBuy/login.png" alt="LogIn">
</br>
<img src="https://res.cloudinary.com/developerteam/image/upload/v1588771339/SimpleBuy/options.png" alt="Options">
</br>
<img src="https://res.cloudinary.com/developerteam/image/upload/v1588771696/SimpleBuy/addresses.png" alt="Addresses">
</br>
<img src="https://res.cloudinary.com/developerteam/image/upload/v1588771849/SimpleBuy/payment-methods.png" alt="PaymentMethods">
</br>
<img src="https://res.cloudinary.com/developerteam/image/upload/v1588771979/SimpleBuy/cart.png" alt="Cart">
</br>
<img src="https://res.cloudinary.com/developerteam/image/upload/v1588772106/SimpleBuy/shopping_1.png" alt="Step1">
</br>
<img src="https://res.cloudinary.com/developerteam/image/upload/v1588772200/SimpleBuy/shopping_2.png" alt="Step2">
</br>
<img src="https://res.cloudinary.com/developerteam/image/upload/v1588772272/SimpleBuy/shopping_3.png" alt="Step3">
</br>
<img src="https://res.cloudinary.com/developerteam/image/upload/v1588772336/SimpleBuy/shopping_4.png" alt="Step4">
</br>
<img src="https://res.cloudinary.com/developerteam/image/upload/v1588772587/SimpleBuy/orders.png" alt="Orders">
</br>
<img src="https://res.cloudinary.com/developerteam/image/upload/v1588772721/SimpleBuy/footer.png" alt="Footer">
</br>
<img src="https://res.cloudinary.com/developerteam/image/upload/v1588772805/SimpleBuy/home-spanish.png" alt="SpanishHome">
</br>

## Try a demo

If you want to try a live and free demo of SimpleBuy, you can do it, just need to go to <a href="https://simplebuy-276303.uc.r.appspot.com" target="_blank">SimpleBuy</a> and you will see a SimpleBuy test version prepared for a testing live. This site is being hosting by Google Cloud Platform.

On this SimpleBuy version you can test the following:

* Home page: It shows a banner with popular brands and products, list of SimpleBuy products, and a footer NavBar with some options like Change Language.
* Sign Up page: It allows you register and create a new SimpleBuy user.
* Login page: It allows you login on SimpleBuy with your user.
* My addresses page: It shows a single page with your shipping addresses, where also you can create, edit, remove, and set like default a shipping address.
* My orders page: On this page you can see your placed orders.
* My payments methods page: On this page you will see your payment methods, which are stored in Stripe, remember SimpleBuy does not store any payment data, this provides security and confidence to our customers.
* Cart page: This page shows all your products in cart, and also it allows you start the shopping process.
* And others little details...

If you want to test the shopping process, you can use the following test cards:

| Number               | Brand              | CVC           | Date             | ZIP    |
| -------------------- | ------------------ | ------------- |----------------- | ------ |
| 4242 4242 4242 4242  | Visa               | Any 3 digits  | Any future date  | 00000  |
| 5555 5555 5555 4444  | Mastercard         | Any 3 digits  | Any future date  | 00000  |
| 3782 822463 10005    | American Express   | Any 3 digits  | Any future date  | 00000  |
  
In case that you need more test cards you can go to <a href="https://stripe.com/docs/testing" target="_blank">Stripe Docs WebSite</a> and get more.

## Have questions?

If you have questions or just need any help, feel free to write to me 
<a href="mailto:hgodinez89@hotmail.com" target="_blank">hgodinez89@hotmail.com</a>

## Thanks

💜 Thanks to <a href="https://stripe.com/" target="_blank">Stripe</a> and <a href="https://cloud.google.com/" target="_blank">GCP</a>.
