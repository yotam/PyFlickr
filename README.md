Downloads images from Flickr with the requested tags. Requires python package [flickrapi](http://stuvel.eu/flickrapi), and a [Flickr API key](http://www.flickr.com/services/apps/create/apply/) (set this in the script).

    usage: flickr.py [-h] -t, TAGS [TAGS ...] [-n QUANTITY] [-o DIRECTORY]

    Download images from Flickr.

    optional arguments:
      -h, --help            show this help message and exit
      -t, TAGS [TAGS ...], --tags TAGS [TAGS ...]
                            tags used to select images
      -n QUANTITY, --quantity QUANTITY
                            number of images required (optional, defaults to 5)
      -o DIRECTORY, --output-dir DIRECTORY
                            output directory (optional, defaults to current)

