import re

print('''
    ---------------------------------------------------------------------
     Hello, in this game, you must enter a few words to describe how a
     story unfolds using only your own words. Be sure to use your
     imagination and pick your words wisely!
    ---------------------------------------------------------------------
          ''')

def read_template(files):
    '''This function reads the file specified by the path and returns
     its content if it exists; otherwise, an error is raised.
     '''
    try:
        with open (files,"r")as file:
            return file.read()
    except:
        raise FileNotFoundError    


   
def parse_template(content):
    '''This function takes the file content and removes the sections 
    enclosed by curly brackets before returning them in a tuple.
    '''
    parts  = re.findall('{(.*?)}', content)
    filterd = re.sub('{.+?}', '{}', content)  
    return filterd,(tuple)(parts)  


def merge (fill_content,parts:tuple):
    '''the user input and the game template are combined by 
    this function, which returns the template with the input.
    '''
    return fill_content.format(*parts)
  
   
def gamefun():
    '''
    This function prints the entire game script with
    the user-added parts and also saves it to a new text file.
    '''
    
    our_game_text = read_template("assets/make_me_a_video_game_template.txt")
    filterd , parts = parse_template(our_game_text)
    print(parts)
    values = list()
    for part in parts:
        values.append(input(f"\n please enter a {part}\n"))
    with open("make_me_a_video_game_template_result.txt",'w') as file:
        game = merge(filterd,(tuple)(values))
        file.write(game)
        print(game)
                        
                
        
    
       
if __name__ =="__main__":
      gamefun() 