from bs4 import BeautifulSoup
import os
import requests
movie_name= input('enter movie:')
url='https://masstamilan.in/{}/'.format(movie_name)

songs=[]
down_link=[]

r = requests.get(url).content
soup= BeautifulSoup(r,'lxml')

h2_tag= soup.find_all('h2',{'class':'nostyle'})

for song in h2_tag:
	songs.append(str(song.find('span').text.strip()))
print(songs)

download_link= soup.find_all('a',{'title':'Download Idhu Varai Naan 320kbps'})

for songlink in download_link:
	down_link.append(songlink.get('href'))

song1= dict(zip(songs,down_link))

num_songs= int(input('1: one song, 2:all song'))

os.chdir('E:\\')

def one_song(n): 
	download= input('enter song name')
	name = song1[download].split('/')[-1]

	r = requests.get(song1[download]).content

	file = open(name, 'wb')
	file.write(r)
	print(name,'Downloaded')

def all_songs():
	for k in down_link:
		name1 = k.split('/')[-1]
		r1 = requests.get(k).content
		file = open(name1, 'wb')
		file.write(r1)
		print('Downloaded',name1)


if num_songs == 1:
	one_song(input('enter song :'))
else:
	all_songs()	