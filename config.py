
import subprocess
import os
import platform

verifications = [
    {0:'curl', 1:'cURL', 2:'curl'},
    {0:'python3', 1:'Python 3', 2:'python3'},
    {0:'pip3', 1:'Pip 3', 2:'pip3'},
    {0:'portaudio19-dev', 1:'portaudio19-dev', 2:'portaudio19-dev'},
    {0:'nvm', 1:'NVM', 2:'curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash'},
    {0:'node', 1:'Node', 2:'nvm install node'},
    {0:'webtorrent', 1:'Web Torrent', 2:'npm install webtorrent-cli -g'}
]

def verify_app(command, app_name, install):
    try:
        subprocess.check_output('{} --version'.format(command), shell=True)
        print('{} are installed!'.format(app_name))
    except:
        print('Installing.. {}'.format(app_name))
        if 'webtorrent' in command or 'nvm' in command or 'node' in command:
            os.system(install)
            if 'nvm' in command:
                os.system('source ~/.profile')
            return
        os.system('sudo apt install {}'.format(install))

def config_spotify():
    print('Now you just need to configure a Spotify Account to the Jarvis..')
    os.system('spotify auth login')

if __name__ == '__main__':
    if 'Linux' in platform.system():
        for verif in verifications:
            verify_app(verif[0], verif[1], verif[2])
        print('======\nNow installing pip requirements..')
        os.system('pip3 install -r requirements.txt')
        #config_spotify()
        print('\n\nJarvis configurado com sucesso! Pressione qualquer tecla para continuar')
    else:
        print('Jarvis only works in Linux machine, sorry.')
        exit()