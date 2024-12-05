import scrapetube
import os
import iascraper



# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

channel_url = 'https://www.youtube.com/@supertfVODs'
videos = scrapetube.get_channel(channel_url=channel_url)

# Construct file paths
results_path = os.path.join(script_dir, "results.sh")
archive_path = os.path.join(script_dir, "alreadyArchived.txt")

#populate the archive file with the items that have been archived from ia
video_identifiers = iascraper.get_video_identifiers()
if video_identifiers:
    with open(archive_path, "w") as archive:
        archive.write('\n'.join(video_identifiers))
        
# Read existing video IDs from the archive file
if os.path.exists(archive_path):
    with open(archive_path, "r") as archive:
        archived_videos = set(archive.read().splitlines())
else:
    archived_videos = set()
    
    
# Empty the results file before the next run
with open(results_path, "w") as f:
    f.write("#!bin/sh \n")
    
    
# Open files using context managers to ensure they are properly closed
with open(results_path, "w") as f, open(archive_path, "r") as archive:
    for video in videos:
        video_id = video.get('videoId')
        if video_id and video_id not in archived_videos:
            f.write(f'\ntubeup -a --cookies=/home/ubuntu/PycharmProjects/cookiesRefresher/cookies.txt "{video_id}"')
            print(video_id)