from mutagen.mp3 import MP3 as mp3
from gtts import gTTS
import pygame
import time
import speech_recognition as sr
import re

while True:
	tts = gTTS("好きな食べ物は何ですか？",lang='ja') #音声作成
	tts.save('会話06.mp3')
	filename = '会話06.mp3' #再生したいmp3ファイル
	pygame.mixer.init()
	pygame.mixer.music.load(filename) #音源を読み込み
	mp3_length = mp3(filename).info.length #音源の長さ取得
	pygame.mixer.music.play(1)
	time.sleep(mp3_length + 0.25)
	pygame.mixer.music.stop() 
	print("好きな食べ物は何ですか？")
	file02 = open('dakara.txt', 'r')  #読み込みモードでオープン
	string02 = file02.read()      #readですべて読み込む
	word02 = string02	# word02に読み込んだテキストデータとreadで読み込んだデータを代入
	r = sr.Recognizer()
	mic = sr.Microphone()
	with mic as source:
    		r.adjust_for_ambient_noise(source)
    		audio = r.listen(source)
	try:
		print(r.recognize_google(audio, language='ja-JP'))	#音声の表示
		before_words02 = r.recognize_google(audio, language='ja-JP') #音声の代入
		after_words02 = re.search(word02, before_words02)
		if re.search(word02, before_words02):
			tts = gTTS(after_words02.group(0) + "が好きなんですね",lang='ja') #音声作成
			tts.save('会話07.mp3')
			filename = '会話07.mp3' #再生したいmp3ファイル
			pygame.mixer.init()
			pygame.mixer.music.load(filename) #音源を読み込み
			mp3_length = mp3(filename).info.length #音源の長さ取得
			pygame.mixer.music.play(1)
			time.sleep(mp3_length + 0.25)
			pygame.mixer.music.stop() 
			print(after_words02.group(0) + "が好きなんですね")
		else:
			tts = gTTS("すいません。その食べ物はデータに該当しません。",lang='ja') #音声作成
			tts.save('会話08.mp3')
			filename = '会話08.mp3' #再生したいmp3ファイル
			pygame.mixer.init()
			pygame.mixer.music.load(filename) #音源を読み込み
			mp3_length = mp3(filename).info.length #音源の長さ取得
			pygame.mixer.music.play(1)
			time.sleep(mp3_length + 0.25)
			pygame.mixer.music.stop() 
			print("すいません。その食べ物はデータに該当しません。")
			continue
	except sr.UnknownValueError:
			tts = gTTS("すいません。上手に聞き取れませんでした。",lang='ja') #音声作成
			tts.save('聞き取り01.mp3')
			filename = '聞き取り01.mp3' #再生したいmp3ファイル
			pygame.mixer.init()
			pygame.mixer.music.load(filename) #音源を読み込み
			mp3_length = mp3(filename).info.length #音源の長さ取得
			pygame.mixer.music.play(1)
			time.sleep(mp3_length + 0.25)
			pygame.mixer.music.stop() 
			print("すいません。上手に聞き取れませんでした。")
			tts = gTTS("もう一度お願いします。",lang='ja') #音声作成
			tts.save('聞き取り02.mp3')
			filename = '聞き取り02.mp3' #再生したいmp3ファイル
			pygame.mixer.init()
			pygame.mixer.music.load(filename) #音源を読み込み
			mp3_length = mp3(filename).info.length #音源の長さ取得
			pygame.mixer.music.play(1)
			time.sleep(mp3_length + 0.25)
			pygame.mixer.music.stop() 
			print("もう一度お願いします。")
			continue
	break