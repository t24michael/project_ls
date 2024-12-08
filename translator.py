from googletrans import Translator
import pyttsx3


class translator:
	def __init__(self, voice, wpm):
		self.voice = voice
		self.voices = {}
		self.wpm = wpm
		self.trans = Translator()
		self.engine = pyttsx3.init()
		self.set_voices()

	def set_voices(self):
		self.voices = {'swedish': "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_svSE_Bengt",
		               'english': "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"}

	def properties(self):
		if self.voice in self.voices:
			self.engine.setProperty('voice', self.voices[self.voice])
			self.engine.setProperty('rate', self.wpm)
		else:
			print("The desired voice is not available! Exiting...")
			exit()

