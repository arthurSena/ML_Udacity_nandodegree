#!/usr/bin/env python

"""
    A script to download photos from a specific instagram profile.
"""

import requests, time, urllib, os, sys, getopt, random
import selenium.webdriver as webdriver 

class instagramCrawler(object):
     """ A instagramCrawler class that manages downloading of photos from 
    a specific  instagram profile.

    Attributes:
        profile     The profile username. 
                    E.g https://www.instagram.com/{username}/
    """
    def __init__(self, profile):
        self.profile = profile

    def run(self, pause_time=3, output_folder=None, amount_of_photos=None):
        """It downloads the amount of photos specified from the instagram profile

            Keyword arguments:
            amount_of_photos -- Amount of photos to be downloaded (default None)
            output_folder -- The folder where the photos will be saved (default None)
            pause_time -- Amount of second to wait until to do the next scroll down.
        """

        output_folder = self.profile + "/" if not output_folder else output_folder

        display = Display(visible=0, size=(800, 600))
        display.start()

        url = 'https://www.instagram.com/' + self.profile

        print "Opening browser..."
        driver = webdriver.Firefox()
        print "Loading web page..."
        driver.get(url)    

        print "Scrolling to the bottom"
        links_set = set()

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(pause_time)

            links = [a.get_attribute('src') for a in driver.find_elements_by_tag_name('img')]
            for l in links:
                links_set.add(l)
            print "Amount of photos' links captured so far: ", len(links_set)

            new_height = driver.execute_script("return document.body.scrollHeight")
            if amount_of_photos: 
                if len(links_set) == amount_of_photos:
                    break
                elif len(links_set) > amount_of_photos:
                    links_set = random.sample(links_set, amount_of_photos)
                    break
            if new_height == last_height:
                break
            last_height = new_height

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for l in links_set:
            print "Getting ", l
            print "Saving in ", os.getcwd() + "/" + output_folder + l.split("/")[-1]
            urllib.urlretrieve(l, output_folder + l.split("/")[-1])
            print 

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "p:a:", ["profile=", "amount-of-photos="])
    except getopt.GetoptError as err:
        print str(err) 
        sys.exit(2)

    profile = None
    amount_of_photos = None
    for o, a in opts:
        if o == "-p":
            profile = a
        elif o == "-a":
            try:
                amount_of_photos = int(a)
            except ValueError as err:
                print "Argument '{}' must be a integer".format(o)
                sys.exit(2)

    crawler = instagramCrawler(profile=profile)
    crawler.run(amount_of_photos=amount_of_photos)

if __name__ == "__main__":
    main()
