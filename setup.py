import os


def header():
    print(
        '''
       ____       _                            
      / ___|  ___| |_ _   _ _ __   _ __  _   _ 
      \___ \ / _ \ __| | | | '_ \ | '_ \| | | |
        __) |  __/ |_| |_| | |_) || |_) | |_| |
      |____/ \___|\__|\__,_| .__(_) .__/ \__, |
                           |_|    |_|    |___/
        Copyright (c) 2022 Juan Carlos Bindez
        
        '''
    )
    
    
 def command(install):
     os.system(install)
     
     
     
command("sudo apt install build-essential libssl-dev libffi-dev python3.10-dev")
command("sudo apt install -y python3.10-venv")
command("sudo apt install python3-virtualenv")
command("virtualenv -p python3.10 venv")
comamnd("source venv/bin/activate")

if __name__ == "__main__":
    header()
