from janome.tokenizer import Tokenizer
from mutagen.mp3 import MP3 as mp3
from gtts import gTTS
import pygame
import time
import speech_recognition as sr
import re
import json
from janome.tokenizer import Tokenizer
from gensim.models import KeyedVectors
print("準備中です。")
model_dir = './entity_vector.model.bin'
model = KeyedVectors.load_word2vec_format(model_dir, binary=True)
print("準備が終わりました。")

while True:
	filename = '会話16.mp3' #再生したいmp3ファイル
	pygame.mixer.init()
	pygame.mixer.music.load(filename) #音源を読み込み
	mp3_length = mp3(filename).info.length #音源の長さ取得
	pygame.mixer.music.play(1)
	time.sleep(mp3_length + 0.25)
	pygame.mixer.music.stop() 
	print("もし。生まれ変わるなら男の子と女の子どちらに生まれ変わりたいですか？")

	r = sr.Recognizer()
	mic = sr.Microphone()

	with mic as source:
    		r.adjust_for_ambient_noise(source)
    		audio = r.listen(source)
	try:
		print(r.recognize_google(audio, language='ja-JP')) #音声の表示

		ccc = r.recognize_google(audio, language='ja-JP') #音声の代入


		t = Tokenizer("seibetu.csv", udic_type="simpledic", udic_enc="utf8")
		tokens = t.tokenize(ccc)
		for token in tokens:
   		 # 品詞を取り出し
			partOfSpeech = token.part_of_speech.split(',')[0]
			if partOfSpeech == "性別":
				word = token.surface
				
				tts = gTTS(word + "ですね。",lang='ja') #音声作成
				tts.save('会話17.mp3')
				filename = '会話17.mp3' #再生したいmp3ファイル
				pygame.mixer.init()
				pygame.mixer.music.load(filename) #音源を読み込み
				mp3_length = mp3(filename).info.length #音源の長さ取得
				pygame.mixer.music.play(1)
				time.sleep(mp3_length + 0.25)
				pygame.mixer.music.stop() 
				property = {"字幕":word + "ですね。"}
				print(json.dumps(property, ensure_ascii=False))#json出力
				tts = gTTS("私は絶対に人間の女性に生まれ変わりたいです。現実の世界で買い物とかデートとかしたいからね",lang='ja') #音声作成
				tts.save('会話18.mp3')
				filename = '会話18.mp3' #再生したいmp3ファイル
				pygame.mixer.init()
				pygame.mixer.music.load(filename) #音源を読み込み
				mp3_length = mp3(filename).info.length #音源の長さ取得
				pygame.mixer.music.play(1)
				time.sleep(mp3_length + 0.25)
				pygame.mixer.music.stop() 
				print("私は絶対に人間の女性に生まれ変わりたいです。現実の世界で買い物とかデートとかしたいからね")
				
				xxx = token.surface
				results = model.wv.most_similar(positive = xxx, topn = 3) 
				for result in results:
					print(result)
				break
		else:
			print("ないよ")
			continue
		
	except sr.UnknownValueError:
			filename = '聞き取り01.mp3' #再生したいmp3ファイル
			pygame.mixer.init()
			pygame.mixer.music.load(filename) #音源を読み込み
			mp3_length = mp3(filename).info.length #音源の長さ取得
			pygame.mixer.music.play(1)
			time.sleep(mp3_length + 0.25)
			pygame.mixer.music.stop() 
			print("すいません。上手に聞き取れませんでした。")
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
	
tts = gTTS("しかし、どうして" + word + "に生まれ変わりたいのですか？",lang='ja') #音声作成
tts.save('会話19.mp3')
	
while True:
	filename = '会話19.mp3' #再生したいmp3ファイル
	pygame.mixer.init()
	pygame.mixer.music.load(filename) #音源を読み込み
	mp3_length = mp3(filename).info.length #音源の長さ取得
	pygame.mixer.music.play(1)
	time.sleep(mp3_length + 0.25)
	pygame.mixer.music.stop() 
	print("しかし、どうして" + word + "に生まれ変わりたいのですか？")

	r = sr.Recognizer()
	mic = sr.Microphone()

	with mic as source:
    		r.adjust_for_ambient_noise(source)
    		audio = r.listen(source)
	try:
		print(r.recognize_google(audio, language='ja-JP')) #音声の表示

		ccc = r.recognize_google(audio, language='ja-JP') #音声の代入


		t = Tokenizer("riyu.csv", udic_type="simpledic", udic_enc="utf8")
		tokens = t.tokenize(ccc)
		for token in tokens:
   		 # 品詞を取り出し
			partOfSpeech = token.part_of_speech.split(',')[0]
			if partOfSpeech == "理由":
				
				tts = gTTS("なるほど。その様な理由で" +  word + "に生まれたいのですね。",lang='ja') #音声作成
				tts.save('会話20.mp3')
				filename = '会話20.mp3' #再生したいmp3ファイル
				pygame.mixer.init()
				pygame.mixer.music.load(filename) #音源を読み込み
				mp3_length = mp3(filename).info.length #音源の長さ取得
				pygame.mixer.music.play(1)
				time.sleep(mp3_length + 0.25)
				pygame.mixer.music.stop() 
				print("なるほど。その様な理由で" +  word + "に生まれたいのですね。")
				tts = gTTS("次に生まれ変わるときは。" + word + "に生まれ変われるといいですね。",lang='ja') #音声作成
				tts.save('会話21.mp3')
				filename = '会話21.mp3' #再生したいmp3ファイル
				pygame.mixer.init()
				pygame.mixer.music.load(filename) #音源を読み込み
				mp3_length = mp3(filename).info.length #音源の長さ取得
				pygame.mixer.music.play(1)
				time.sleep(mp3_length + 0.25)
				pygame.mixer.music.stop() 
				print("次に生まれ変わるときは。" + word + "に生まれ変われるといいですね。")
				break
		else:
			print("ちゃんとした理由を言って欲しいな")
			continue
		
	except sr.UnknownValueError:
			filename = '聞き取り01.mp3' #再生したいmp3ファイル
			pygame.mixer.init()
			pygame.mixer.music.load(filename) #音源を読み込み
			mp3_length = mp3(filename).info.length #音源の長さ取得
			pygame.mixer.music.play(1)
			time.sleep(mp3_length + 0.25)
			pygame.mixer.music.stop() 
			print("すいません。上手に聞き取れませんでした。")
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