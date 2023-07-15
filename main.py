from TTS.api import TTS

def textToSpeech(text):
    tts = TTS(TTS.list_models()[0])
    # to pt-br
    tts.tts_to_file(text=text, speaker=tts.speakers[2], language='pt-br', file_path="output.wav")

text = 'Após polêmica, Governo rejeita proposta de Bolsonaro e mantém auxílio Brasil'

textToSpeech(text)