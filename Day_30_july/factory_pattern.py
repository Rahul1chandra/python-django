# we want to open an file
# based on the file extenstion we have to open the respective application
#   .txt ==  notepad, .mp3  == vlc media player, doc = mScdSoc 
#  opening any file doble click (open) media player


player_extension = {
    ".txt" : "Notepad()",
    ".doc" : "Document()",
    ".mp3" : "Mp3()"
}

class Player:
    def play(self):
        pass

class Notepad(Player):
    def play(self):
        return ("inside notepad player")

class Document(Player):
    def play(self):
        return ("inside document Player")
    
class Mp3(Player):
    def play(self):
        return("inside my Mp3")


file_name = input("open file name ")
### we will get the file extension 
### based on the extension we will call the method 

file_extension  = file_name[-4:]
obj = eval(player_extension[file_extension])
print (obj.play())








