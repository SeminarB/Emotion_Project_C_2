from mutagen.mp3 import MP3 as mp3
from gtts import gTTS
import pygame
import time
import re
#input(">>>")
tts = gTTS("こんにちは",lang='ja') #音声作成
tts.save('ko01.mp3')
filename = 'ko01.mp3' #再生したいmp3ファイル
pygame.mixer.init()
pygame.mixer.music.load(filename) #音源を読み込み
mp3_length = mp3(filename).info.length #音源の長さ取得
pygame.mixer.music.play(1) #再生開始。1の部分を変えるとn回再生(その場合は次の行の秒数も×nすること)
time.sleep(mp3_length + 0.25) #再生開始後、音源の長さだけ待つ(0.25待つのは誤差解消)
pygame.mixer.music.stop() #音源の長さ待ったら再生停止
print("こんにちは")
tts = gTTS("私はエリナといいます",lang='ja') #音声作成
tts.save('Hola10.mp3')
filename = 'Hola10.mp3' #再生したいmp3ファイル
pygame.mixer.init()
pygame.mixer.music.load(filename) #音源を読み込み
mp3_length = mp3(filename).info.length #音源の長さ取得
pygame.mixer.music.play(1) #再生開始。1の部分を変えるとn回再生(その場合は次の行の秒数も×nすること)
time.sleep(mp3_length + 0.25) #再生開始後、音源の長さだけ待つ(0.25待つのは誤差解消)
pygame.mixer.music.stop() #音源の長さ待ったら再生停止
print("私はエリナといいます")
tts = gTTS("あなたの名前はなんと言うのですか？",lang='ja') #音声作成
tts.save('Hola21.mp3')
filename = 'Hola21.mp3' #再生したいmp3ファイル
pygame.mixer.init()
pygame.mixer.music.load(filename) #音源を読み込み
mp3_length = mp3(filename).info.length #音源の長さ取得
pygame.mixer.music.play(1) #再生開始。1の部分を変えるとn回再生(その場合は次の行の秒数も×nすること)
time.sleep(mp3_length + 0.25) #再生開始後、音源の長さだけ待つ(0.25待つのは誤差解消)
pygame.mixer.music.stop() #音源の長さ待ったら再生停止
print("あなたの名前はなんと言うのですか？")
xxx = input("呼ばれたい名前を入力してください>>>")
tts = gTTS("%sさんですね"% xxx,lang='ja') #音声作成
tts.save('Hola26.mp3')
filename = 'Hola26.mp3' #再生したいmp3ファイル
pygame.mixer.init()
pygame.mixer.music.load(filename) #音源を読み込み
mp3_length = mp3(filename).info.length #音源の長さ取得
pygame.mixer.music.play(1) #再生開始。1の部分を変えるとn回再生(その場合は次の行の秒数も×nすること)
time.sleep(mp3_length + 0.25) #再生開始後、音源の長さだけ待つ(0.25待つのは誤差解消)
pygame.mixer.music.stop() #音源の長さ待ったら再生停止
print("%sさんですね"% xxx)
tts = gTTS("%sさんは何歳ですか？"% xxx,lang='ja') #音声作成
tts.save('Hola22.mp3')
filename = 'Hola22.mp3' #再生したいmp3ファイル
pygame.mixer.init()
pygame.mixer.music.load(filename) #音源を読み込み
mp3_length = mp3(filename).info.length #音源の長さ取得
pygame.mixer.music.play(1) #再生開始。1の部分を変えるとn回再生(その場合は次の行の秒数も×nすること)
time.sleep(mp3_length + 0.25) #再生開始後、音源の長さだけ待つ(0.25待つのは誤差解消)
pygame.mixer.music.stop() #音源の長さ待ったら再生停止
print("%sさんは何歳ですか？"% xxx)
sss = input("あなたの年齢を入力してください>>>") #文字列の検索値
m = re.search("18|19|20|21|22|23|24|25",sss)	#指定値のみを検索
ooo = m.group()
words = '私は18歳です私は19歳です私は20歳です私は21歳です私は22歳です私は23歳です私は24歳私はです私は25歳ですだよだぜ' #文字列の検索
if sss in words: 
	tts = gTTS("%sさんは%s歳なんですね！"% (xxx,ooo),lang='ja') #音声作成
	tts.save('Hola145.mp3')
	filename = 'Hola145.mp3' #再生したいmp3ファイル
	pygame.mixer.init()
	pygame.mixer.music.load(filename) #音源を読み込み
	mp3_length = mp3(filename).info.length #音源の長さ取得
	pygame.mixer.music.play(1) #再生開始。1の部分を変えるとn回再生(その場合は次の行の秒数も×nすること)
	time.sleep(mp3_length + 0.25) #再生開始後、音源の長さだけ待つ(0.25待つのは誤差解消)
	pygame.mixer.music.stop() #音源の長さ待ったら再生停止
	print("%sさんは%s歳なんですね！"% (xxx,ooo))
tts = gTTS("私は、20歳です",lang='ja') #音声作成
tts.save('Hola66.mp3')
filename = 'Hola66.mp3' #再生したいmp3ファイル
pygame.mixer.init()
pygame.mixer.music.load(filename) #音源を読み込み
mp3_length = mp3(filename).info.length #音源の長さ取得
pygame.mixer.music.play(1) #再生開始。1の部分を変えるとn回再生(その場合は次の行の秒数も×nすること)
time.sleep(mp3_length + 0.25) #再生開始後、音源の長さだけ待つ(0.25待つのは誤差解消)
pygame.mixer.music.stop() #音源の長さ待ったら再生停止
print("私は、20歳です")
tts = gTTS("%sさんは好きな食べ物はありますか？"% xxx,lang='ja') #音声作成
tts.save('Hola67.mp3')
filename = 'Hola67.mp3' #再生したいmp3ファイル
pygame.mixer.init()
pygame.mixer.music.load(filename) #音源を読み込み
mp3_length = mp3(filename).info.length #音源の長さ取得
pygame.mixer.music.play(1) #再生開始。1の部分を変えるとn回再生(その場合は次の行の秒数も×nすること)
time.sleep(mp3_length + 0.25) #再生開始後、音源の長さだけ待つ(0.25待つのは誤差解消)
pygame.mixer.music.stop() #音源の長さ待ったら再生停止
print("%sさんは好きな食べ物はありますか？"% xxx)
ppp = input("")
words = '私はりんごが好きですりんごです私はりんごが大好きです' #文字列の検索
www = "私はみかんが好きです私はみかんが好きですみかんが大好きです"
uiui = "私はバナナが好きです私はバナナが好きですバナナが大好きです"
if ppp in words: 
	tts = gTTS("%sさんはりんごが好きなのですね！　私もりんごは大好きです！"% xxx,lang='ja') #音声作成
	tts.save('Hola93.mp3')
	filename = 'Hola93.mp3' #再生したいmp3ファイル
	pygame.mixer.init()
	pygame.mixer.music.load(filename) #音源を読み込み
	mp3_length = mp3(filename).info.length #音源の長さ取得
	pygame.mixer.music.play(1) #再生開始。1の部分を変えるとn回再生(その場合は次の行の秒数も×nすること)
	time.sleep(mp3_length + 0.25) #再生開始後、音源の長さだけ待つ(0.25待つのは誤差解消)
	pygame.mixer.music.stop() #音源の長さ待ったら再生停止
	print("%sさんですね"% xxx)
elif ppp in www: 
	tts = gTTS("%sさんはみかんが好きなのですね！私は前に食べたとき、とてもしょっぱくてそれ以来好きじゃありません。"% xxx,lang='ja') #音声作成
	tts.save('Hola94.mp3')
	filename = 'Hola94.mp3' #再生したいmp3ファイル
	pygame.mixer.init()
	pygame.mixer.music.load(filename) #音源を読み込み
	mp3_length = mp3(filename).info.length #音源の長さ取得
	pygame.mixer.music.play(1) #再生開始。1の部分を変えるとn回再生(その場合は次の行の秒数も×nすること)
	time.sleep(mp3_length + 0.25) #再生開始後、音源の長さだけ待つ(0.25待つのは誤差解消)
	pygame.mixer.music.stop() #音源の長さ待ったら再生停止
	print("%sさんはみかんが好きなのですね！私は前に食べたとき、とてもしょっぱくてそれ以来好きじゃありません。"% xxx)
elif ppp in uiui: 
	tts = gTTS("%sさんはバナナが好きなのですね。私はバナナが大好物です。朝ごはんにいつも食べてます！"% xxx,lang='ja') #音声作成
	tts.save('Hola95.mp3')
	filename = 'Hola95.mp3' #再生したいmp3ファイル
	pygame.mixer.init()
	pygame.mixer.music.load(filename) #音源を読み込み
	mp3_length = mp3(filename).info.length #音源の長さ取得
	pygame.mixer.music.play(1) #再生開始。1の部分を変えるとn回再生(その場合は次の行の秒数も×nすること)
	time.sleep(mp3_length + 0.25) #再生開始後、音源の長さだけ待つ(0.25待つのは誤差解消)
	pygame.mixer.music.stop() #音源の長さ待ったら再生停止
	print("%sさんはバナナが好きなのですね。私はバナナが大好物です。朝ごはんにいつも食べてます！"% xxx)
tts = gTTS("%sさんとお話ができて楽しかったです。またお話しましょう！　さようなら"% xxx,lang='ja') #音声作成
tts.save('Hola66.mp3')
filename = 'Hola66.mp3' #再生したいmp3ファイル
pygame.mixer.init()
pygame.mixer.music.load(filename) #音源を読み込み
mp3_length = mp3(filename).info.length #音源の長さ取得
pygame.mixer.music.play(1) #再生開始。1の部分を変えるとn回再生(その場合は次の行の秒数も×nすること)
time.sleep(mp3_length + 0.25) #再生開始後、音源の長さだけ待つ(0.25待つのは誤差解消)
pygame.mixer.music.stop() #音源の長さ待ったら再生停止
print("%sさんとお話ができて楽しかったです。またお話しましょう！それではさようなら!!"% xxx)