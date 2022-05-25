from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
from tempfile import gettempdir
from playsound import playsound
from gtts import gTTS
from time import sleep

#Google Text-to-Speech
def text_to_audio(data):
    audio = gTTS(text=data, lang='pt', slow=False)
    audio.save("voice.mp3")
    output = os.path.join("", "voice.mp3")
    playsound(output)
    sleep(0.5)
    os.remove('voice.mp3')
    return

#Amazon Polly (AWS)
""" def text_to_audio(data):
    session = Session(profile_name="default")
    polly = session.client("polly")
    try:
        response = polly.synthesize_speech(Text=data, OutputFormat="mp3",
                                            VoiceId="Ricardo")
    except (BotoCoreError, ClientError) as error:
        # The service returned an error, exit gracefully
        print(error)
        sys.exit(-1)
    if "AudioStream" in response:
    # Note: Closing the stream is important because the service throttles on the
    # number of parallel connections. Here we are using contextlib.closing to
    # ensure the close method of the stream object will be called automatically
    # at the end of the with statement's scope.
        with closing(response["AudioStream"]) as stream:
           output = os.path.join(gettempdir(), "speech.mp3")
           try:
            # Open a file for writing the output as a binary stream
                with open(output, "wb") as file:
                   file.write(stream.read())
           except IOError as error:
              # Could not write to file, exit gracefully
              print(error)
              sys.exit(-1)
    else:
        # The response didn't contain audio data, exit gracefully
        print("Could not stream audio")
        sys.exit(-1)
    # Play the audio using the platform's default player
    if sys.platform == "win32":
        os.startfile(output)
    else:
        # The following works on macOS and Linux. (Darwin = mac, xdg-open = linux).
        playsound(output)
        return
     """