import pywhatkit
import datetime

mobile_number = input("Please tell me the 10-digit mobile number of the recipient: ")
mobile_number = mobile_number.replace(' ', '').replace('+91', '')
if not mobile_number.isdigit() or len(mobile_number) != 10:
    print("Invalid mobile number. Please enter a valid 10-digit mobile number.")
else:
    message = input("Tell me your message: ")
    if not message:
        print("Please provide a message.")
    else:
        print("Opening WhatsApp web to send your message...")
        print("Please be patient, sometimes it takes time.\nOR In some cases, it does not work.")
        try:
            pywhatkit.sendwhatmsg("+91" + mobile_number, message, datetime.datetime.now().hour, datetime.datetime.now().minute + 1)
            print('Message sent successfully.')
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Error: Message not sent. Please try again.")
