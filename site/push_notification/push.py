__author__ = 'chance'

from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AAAARAUK_1U:APA91bEWDFmhqWVEicI1xWh7R41lB8DGyjiRrLlfaa-CqLtMLvbGzLtL6nCBYgXVKKuiLas8hsX6YnHFQUoWqHZS_crAssz2B-msCzOAYqWqsTuc9AgPnTJL0OtPnEjBG9FC4hFd9339")


print("Hello")

# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

registration_id = "fyOoafoZVl8:APA91bHk3CwpzBXTKbEZiFs6i57NZqnSDPrkA0vZI-rUbMmK6t1ov9bhqFULtLOUAfi0BXs0y4VCoRiu1nBdo82NK7iDCcIkMnV7eqpTDOP3a9X3bmMCPb4gk0OSIGPl5UANaOKFQjNl"
message_title = "Python test 1"
message_body = "Hello python test 1"
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body,sound="Default", topic_name="Test2")

print (result)