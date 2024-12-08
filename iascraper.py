from internetarchive import search_items


def get_video_identifiers():
    identifiers = []
    for i in search_items('channel:supertfVODs'):
        identifier = i['identifier'].split('youtube-')[-1].split('oauth2-')[-1]
        identifiers.append(identifier)
        #print(i['identifier'].split('youtube-')[-1].split('oauth2-')[-1])
    return identifiers
    

#get_video_identifiers()


# def get_video_urls():
#     counter = 0
#     for item in search_items('channel:supertfVODs').iter_as_items():
#         #print(item.item_metadata['metadata']['originalurl']) # use .split('=')[-1] to get the video id
#         print(f'{item.item_metadata['item_size']}')
#         counter += 1
#         break
#     print(counter)

# get_video_urls() #this is slower

def get_video_urls():
    for item in search_items(query='channel:supertfVODs',params='item_size').iter_as_items():
        item_size = item.item_metadata['item_size']
        original_url = item.item_metadata['metadata']['originalurl']
        #if item_size < 100000000:
        print(f"Item Size: {item_size}, Original URL: {original_url}")

# get items that are less than 100MB
#get_video_urls()