"""Broadcast Settings."""

from src.masonite import env

"""Broadcast Driver
Realtime support is critical for any modern web application. Broadcast
drivers allow you to push data from your server to all your clients
to show data updates to your clients in real time without having
to constantly refresh the page or send constant ajax requests

Supported: 'pusher', 'ably', 'pubnub'
"""

DRIVER = env('BROADCAST_DRIVER', 'pusher')

"""Broadcast Drivers
Below is a dictionary of all your driver configurations. Each key in the
dictionary should be the name of a driver.
"""

DRIVERS = {
    'pusher': {
        'app_id': env('PUSHER_APP_ID', '29382xx..'),
        'client': env('PUSHER_CLIENT', 'shS8dxx..'),
        'secret': env('PUSHER_SECRET', 'HDGdjss..'),
        'cluster': env('PUSHER_CLUSTER', 'eu'),
    },
    'ably': {
        'secret': env('ABLY_SECRET', 'api:key')
    },
    'pubnub': {
        'secret': env('PUBNUB_SECRET', ''),
        'publish_key': env('PUBNUB_PUBLISH_KEY', ''),
        'subscribe_key': env('PUBNUB_SUBSCRIBE_KEY', '')
    }
}
