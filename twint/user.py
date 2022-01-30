import datetime
import logging as logme


class user:
    type = "user"

    def __init__(self):
        pass


User_formats = {
    'join_date': '%Y-%m-%d',
    'join_time': '%H:%M:%S %Z'
}


# ur object must be a json from the endpoint https://api.twitter.com/graphql
def User(ur):
    logme.debug(__name__ + ':User')
    if 'data' not in ur and 'user' not in ur['data']:
        msg = 'malformed json! cannot be parsed to get user data'
        logme.fatal(msg)
        raise KeyError(msg)
    _usr = user()
    if 'rest_id' in ur['data']['user']:
        _usr.id = ur['data']['user']['rest_id']
    else:
        _usr.id = None
    if 'name' in ur['data']['user']['legacy']:
        _usr.name = ur['data']['user']['legacy']['name']
    else:
        _usr.name = None
    if 'screen_name' in ur['data']['user']['legacy']:
        _usr.username = ur['data']['user']['legacy']['screen_name']
    else:
        _usr.username = None
    if 'description' in ur['data']['user']['legacy']:
        _usr.bio = ur['data']['user']['legacy']['description']
    else:
        _usr.bio = None
    if 'location' in ur['data']['user']['legacy']:
        _usr.location = ur['data']['user']['legacy']['location']
    else:
        _usr.location = None
    if 'url' in ur['data']['user']['legacy']:
        _usr.url = ur['data']['user']['legacy']['url']
    else:
        _usr.url = None
    # parsing date to user-friendly format
    if 'created_at' in ur['data']['user']['legacy']:
        _dt = ur['data']['user']['legacy']['created_at']
        _dt = datetime.datetime.strptime(_dt, '%a %b %d %H:%M:%S %z %Y')
    else:
        _dt = None
    # date is of the format year,
    if 'join_date' in User_formats:
        _usr.join_date = _dt.strftime(User_formats['join_date'])
    else:
        _usr.join_date = None
    if 'join_time' in User_formats:
        _usr.join_time = _dt.strftime(User_formats['join_time'])
    else:
        _usr.join_time = None

    # :type `int`
    if 'statuses_count' in ur['data']['user']['legacy']:
        _usr.tweets = int(ur['data']['user']['legacy']['statuses_count'])
    else:
        _usr.tweets = None
    if 'friends_count' in ur['data']['user']['legacy']:
        _usr.following = int(ur['data']['user']['legacy']['friends_count'])
    else:
        _usr.following = None
    if 'followers_count' in ur['data']['user']['legacy']:
        _usr.followers = int(ur['data']['user']['legacy']['followers_count'])
    else:
        _usr.followers = None
    if 'favourites_count' in ur['data']['user']['legacy']:
        _usr.likes = int(ur['data']['user']['legacy']['favourites_count'])
    else:
        _usr.likes = None
    if 'media_count' in ur['data']['user']['legacy']:
        _usr.media_count = int(ur['data']['user']['legacy']['media_count'])
    else:
        _usr.media_count = None

    if 'protected' in ur['data']['user']['legacy']:
        _usr.is_private = ur['data']['user']['legacy']['protected']
    else:
        _usr.is_private = None
    if 'verified' in ur['data']['user']['legacy']:
        _usr.is_verified = ur['data']['user']['legacy']['verified']
    else:
        _usr.is_verified = None
    if 'profile_image_url_https' in ur['data']['user']['legacy']:
        _usr.avatar = ur['data']['user']['legacy']['profile_image_url_https']
    else:
        _usr.avatar = None
    if 'profile_banner_url' in ur['data']['user']['legacy']:
        _usr.background_image = ur['data']['user']['legacy']['profile_banner_url']
    else:
        _usr.background_image = None
    # TODO : future implementation
    # legacy_extended_profile is also available in some cases which can be used to get DOB of user
    return _usr
