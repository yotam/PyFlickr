#!/usr/bin/env python
import flickrapi
import itertools
import urllib
import argparse
import os

API_KEY = "KEY GOES HERE"

def retrieve(n_images, tags, directory):
    flickr = flickrapi.FlickrAPI(API_KEY)
    for p in itertools.islice(flickr.walk(tag_mode='all' ,tags=','.join(tags), extras="url_l"), n_images):
        url =  'http://farm%s.static.flickr.com/%s/%s_%s_%s.jpg' % \
        (p.get('farm'), p.get('server'), p.get('id'), p.get('secret'), "b")
        print url
        urllib.urlretrieve(url,os.path.join(directory, p.get('id') + '.jpg'))

def main():
    parser = argparse.ArgumentParser(description='Download images from Flickr.')
    parser.add_argument('-t,', '--tags', dest='tags', nargs='+', required=True,
    help='tags used to select images')
    parser.add_argument('-n','--quantity', type=int, dest='quantity', default=5,
    help='number of images required (optional, defaults to 5)')
    parser.add_argument('-o','--output-dir', dest='directory', default=os.path.curdir,
    help='output directory (optional, defaults to current)')
    args = parser.parse_args()
    
    if os.path.exists(os.path.expanduser(args.directory)):
        print 'retrieving %d photos tagged with %s' % (args.quantity, ', '.join(args.tags))
        retrieve(args.quantity, args.tags, args.directory)
    else:
        print 'invalid directory'

if __name__ == "__main__":
    main()
