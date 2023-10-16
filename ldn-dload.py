import argparse
import requests
import urllib.request
import multiprocessing
import ThreadPool

URL = "https://dts.podtrac.com/redirect.mp3/files.lagedernation.org/lagedernation/LdN001.mp3?ptm_source=feed&ptm_context=mp3&ptm_file=LdN001.mp3"

def main():
    parser = argparse.ArgumentParser(description="download specific episodes from Lage der Nation")
    parser.add_argument("start", type=int, help="specifies which episode to start the download from.")
    parser.add_argument("stop", type=int, help="specifies the episode which is the last to download")
    parser.add_argument("-v", "--verbosity", action="count", default = 0, help="explains what the program is doing")
    args = parser.parse_args()
  
    if args.verbosity > 0:
        print(f"starting download from episode {args.start} to episode {args.stop}...")
        verbose = True
    else:
        verbose = False

    # writeFile("https://dts.podtrac.com/redirect.mp3/files.lagedernation.org/lagedernation/LdN001.mp3?ptm_source=feed&ptm_context=mp3&ptm_file=LdN001.mp3")

    # ldn_request = requests.get(URL, stream=True)
    
    # chunk_size = 256
    # with open ("ldn_test_2.mp3", "wb") as f:
    #     for chunk in ldn_request.iter_content(chunk_size):
    #         f.write(chunk)



    downloadSourceFile(args.start, args.stop, verbose)


    return 0

# def load(url):
#     req = urllib.request.Request(url)
#     return urllib.request.urlopen(req).read()
#     # with open("ldn_test_2.mp3", "wb") as f:
#     #     f.write(req)

# def writeFile(url):
#     data = load(url)
#     with open("ldn_test_4.mp3", "wb") as f:
#         f.write(data)
        
def downloadSource(url):
    ldn_request = urllib.request.Request(url)
    return urllib.request.urlopen(ldn_request).read()

def writeFile(data, file_name):
    with open(file_name, "wb") as f:
        f.write(data)

def downloadSourceFile(episode_low_nr, episode_high_nr, verbose=False):
    source_first = "https://dts.podtrac.com/redirect.mp3/files.lagedernation.org/lagedernation/LdN"
    source_second = ".mp3?ptm_source=feed&ptm_context=mp3&ptm_file=LdN"
    source_last = ".mp3"

    background_tasks = set()

    for episode in range(episode_low_nr, episode_high_nr+1):
        if (episode < 10):
            episode_string = "00"+str(episode)

        if (episode > 9 and episode < 100):
            episode_string = "0"+str(episode)

        if (episode > 100):
            episode_string = str(episode)

        source_full = source_first+str(episode_string)+source_second+str(episode_string)+source_last
        file_name = "LdN"+episode_string+".mp3"

        if verbose:
            print(f"downloading {file_name}...")

        writeFile(downloadSource(source_full), file_name)
        # data = downloadSource(source_full)a
        # writeFile(data, file_name)
        # LdN352.mp3
# test

# https://dts.podtrac.com/redirect.mp3/files.lagedernation.org/lagedernation/LdN352.mp3?ptm_source=feed&ptm_context=mp3&ptm_file=LdN352.mp3


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass




# source url:
# https://dts.podtrac.com/redirect.mp3/files.lagedernation.org/lagedernation/LdN352.mp3?ptm_source=feed&ptm_context=mp3&ptm_file=LdN352.mp3

# LdN feed:
# https://feeds.lagedernation.org/feeds/ldn-mp3.xml