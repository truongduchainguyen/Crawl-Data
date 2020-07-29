from scraper import extract

page = 'https://www.facebook.com/PhilipsLightingVietnam/'
comments = 'y'
list = extract(page, 30, comments)