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
    if 'name' in ur['data']['user']['legacy']:
        _usr.name = ur['data']['user']['legacy']['name']
    if 'screen_name' in ur['data']['user']['legacy']:
        _usr.username = ur['data']['user']['legacy']['screen_name']
    if 'description' in ur['data']['user']['legacy']:
        _usr.bio = ur['data']['user']['legacy']['description']
    if 'location' in ur['data']['user']['legacy']:
        _usr.location = ur['data']['user']['legacy']['location']
    if 'url' in ur['data']['user']['legacy']:
        _usr.url = ur['data']['user']['legacy']['url']
    # parsing date to user-friendly format
    if 'created_at' in ur['data']['user']['legacy']:
        _dt = ur['data']['user']['legacy']['created_at']
    if 'user' in ur['data']:
        _dt = datetime.datetime.strptime(_dt, '%a %b %d %H:%M:%S %z %Y')
    # date is of the format year,
    if 'join_date' in User_formats:
        _usr.join_date = _dt.strftime(User_formats['join_date'])
    if 'join_time' in User_formats:
        _usr.join_time = _dt.strftime(User_formats['join_time'])

    # :type `int`
    if 'statuses_count' in ur['data']['user']['legacy']:
        _usr.tweets = int(ur['data']['user']['legacy']['statuses_count'])
    if 'friends_count' in ur['data']['user']['legacy']:
        _usr.following = int(ur['data']['user']['legacy']['friends_count'])
    if 'followers_count' in ur['data']['user']['legacy']:
        _usr.followers = int(ur['data']['user']['legacy']['followers_count'])
    if 'favourites_count' in ur['data']['user']['legacy']:
        _usr.likes = int(ur['data']['user']['legacy']['favourites_count'])
    if 'media_count' in ur['data']['user']['legacy']:
        _usr.media_count = int(ur['data']['user']['legacy']['media_count'])

    if 'protected' in ur['data']['user']['legacy']:
        _usr.is_private = ur['data']['user']['legacy']['protected']
    if 'verified' in ur['data']['user']['legacy']:
        _usr.is_verified = ur['data']['user']['legacy']['verified']
    if 'profile_image_url_https' in ur['data']['user']['legacy']:
        _usr.avatar = ur['data']['user']['legacy']['profile_image_url_https']
    if 'profile_banner_url' in ur['data']['user']['legacy']:
        _usr.background_image = ur['data']['user']['legacy']['profile_banner_url']
    # TODO : future implementation
    # legacy_extended_profile is also available in some cases which can be used to get DOB of user
    return _usr
