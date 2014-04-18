# -*- coding: utf-8 -*-

from libs.map import Map
from libs.inputoutput import arguments

from os import path,makedirs


(items, frame, prior, codes, working_directory) = arguments(path.dirname(path.realpath(__file__)),True)

for item in items:
    m = Map(working_directory, frame, place_asked=int(item),codes=codes)

<<<<<<< HEAD
=======
if args.file is None:
    working_directory = path.dirname(path.realpath(__file__))
else:
    working_directory = args.file
frame = inputoutput.load_geo_csv(working_directory+"/geography.answer.csv")
codes = inputoutput.load_general_csv(path=working_directory+'/geography.place.csv',names=['id','code','name','type'],skip_rows=1)

for item in args.items:
    m = Map(path=working_directory, codes=codes, df=frame, place_asked=int(item))

>>>>>>> 101963544307ed1c158181f775020dd1a28a530e
    directory = working_directory+'/maps/place/'+item+'/'
    if not path.exists(directory):
        makedirs(directory)

    print 'Generating maps for place',item
<<<<<<< HEAD
    m.mistaken_countries(path=directory)
=======
    m.mistaken_countries(path=directory)
>>>>>>> 101963544307ed1c158181f775020dd1a28a530e
