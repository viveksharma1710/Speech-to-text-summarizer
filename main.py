import speech_to_text
import summarizer

print('Converting audio transcripts into text....')

speech_to_text.s2t("sample.wav")

summarizer.summarise("sample.txt")
