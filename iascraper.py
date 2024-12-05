from internetarchive import search_items


def get_video_identifiers():
    identifiers = []
    for i in search_items('channel:supertfVODs'):
        identifier = i['identifier'].split('youtube-')[-1].split('oauth2-')[-1]
        identifiers.append(identifier)
        #print(i['identifier'].split('youtube-')[-1].split('oauth2-')[-1])
    return identifiers
    

get_video_identifiers()


def get_video_urls():
    counter = 0
    for item in search_items('channel:supertfVODs').iter_as_items():
        print(item.item_metadata['metadata']['originalurl']) # use .split('=')[-1] to get the video id
        counter += 1
    print(counter)

# get_video_urls() #this is slower
