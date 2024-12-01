from pynput.keyboard import Listener, Key
import ctypes




class KeyboardListener:
   
    def __init__(self):
        self.target_stop = 'stop'
        self.target_sequence = 'choco'
        self.current_sequence = ''
        self.listener = Listener(on_press=self.on_press)
        
    def on_press(self, key):
  
       
        try:
            if key == Key.backspace:
                    self.current_sequence = self.current_sequence[0:-1]  #touche effacer
                    print('Touche supprimer')  


            char = key.char  # Obtient le caractère de la touche pressée
           
           
            if char:
                if key == Key.backspace:
                    self.current_sequene = self.current_sequence[0:-1]  
                    
                else:          
                    self.current_sequence += char
                    print(f"Vous avez tapé: {self.current_sequence}")
                

                # Vérifie si la séquence tapée correspond à "choco"
                if self.current_sequence[-5:] == self.target_sequence:
                    print("Vous avez bien tapé 'choco' !")
                    self.current_sequence = ''  # Réinitialise la séquence pour permettre une nouvelle détection 
                    ctypes.windll.user32.LockWorkStation()
                    return False


                # Vérifie si la séquence tapée correspond à "tstop"
                if self.current_sequence[-4:] == self.target_stop:
                    print("Vous avez bien tapé 'stop' !") 
                    self.current_sequence = '' # Réinitialise la séquence pour permettre une nouvelle détection
                    return False




        except AttributeError:
            print(f"Une touche spéciale {key} est pressée.")

    def run(self):
        # Démarre l'écoute
        self.listener.start()
        self.listener.join()


# Création de l'instance et lancement de l'écoute
keyboard = KeyboardListener()
keyboard.run()