import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Load the service account key
cred = credentials.Certificate('chirpchat-23dba-firebase-adminsdk-kh0p1-529b03f269.json')

# Initialize the Firebase app
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://chirpchat-23dba-default-rtdb.firebaseio.com/'
})

# Get a reference to the database
root = db.reference()

# Create the "/messages" node if it doesn't exist
messages_node = root.child('messages')
if messages_node.get() is None:
    messages_node.set({})

# Function to send a message
def send_message(text):
    new_message = messages_node.push({
        'text': text
    })
    print(f'Sent message: {text}')

# Function to retrieve the latest messages
def retrieve_messages():
    messages = messages_node.order_by_key().limit_to_last(10).get()
    print('Latest messages:')
    for message_id in reversed(list(messages.keys())):
        message = messages[message_id]
        print(f'{message["text"]}')

# Main loop
while True:
    command = input('Enter a command (send [text], retrieve, quit): ')
    if command.startswith('send '):
        text = command[5:]
        send_message(text)
    elif command == 'retrieve':
        retrieve_messages()
    elif command == 'quit':
        break
    else:
        print('Unknown command')
