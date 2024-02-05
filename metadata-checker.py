import os, music_tag
directory = r'C:\Users\micro\Music\my music\music\artists'

relevant_traits = ['title', 'artist', 'album', 'tracknumber', 'albumartist']
need_fixing = []

def check_if_audio(filename):
        audio_names = ['.aac', '.aiff', '.dsf', '.flac', '.m4a', '.mp3', '.ogg', '.opus', '.wav']
        for name in audio_names:
                if filename.endswith(name):
                        return True    
        return False 

def fix_tracknumber(filename):
        new_tracknumber = ''
        is_beginning = True
        for char in filename:
                if char.isdigit() and is_beginning:
                        new_tracknumber += char
                else:
                        is_beginning = False
        return(new_tracknumber)

def fix_title(filename):
        new_name = filename
        new_name = new_name.strip(' ')
        new_name = new_name.split('.', 1)[0]
        ind = 0
        is_beginning = True
        for char in new_name:
                if char == '_' or char == '-':
                        new_name = new_name[: ind] + ' ' + new_name[ind + 1:]
                        new_name = new_name[:ind + 1] + new_name[ind + 1].upper() + new_name[ind + 2:]
                        is_beginning = False
                elif char.isdigit() and is_beginning:
                        new_name = new_name[: ind] + '' + new_name[ind + 1:]
                        ind = ind - 1
                else:
                        if is_beginning == True:
                                new_name = new_name[ind].upper() + new_name[ind + 1:]
                        is_beginning = False
                        
                ind = ind + 1
        new_name = new_name.strip(' ')
        return(new_name)

def same_album_check(main, checked):
        if main['album']:
                if main['album'] == checked['album']:
                        pass
                if main['year'] and main['year'] != checked['year']:
                        return False
                if main['year'] and main['year'] != checked['year']:
                        return False
        else:
                return False
                
def fix_totaltracks(s):
        net_tracks = 0
        for file in os.listdir(directory):
                if music_tag.load_file(file)['album'] == s['album']:
                        net_tracks += 1
        return(net_tracks)

def autofix(s, filename, trait, initial):
        if trait == 'title':
                s[trait] = fix_title(filename)
        if trait == 'tracknumber':
                s[trait] = fix_tracknumber(filename)
        if trait == 'albumartist' and s['artist']:
                s[trait] = s['artist']
        if trait == 'artist' and s['albumartist']:
                s[trait] = s['albumartist']
        if trait == 'totaltracks':
                s[trait] = fix_totaltracks(s)
        if s[trait]:
                s.save()
                return True
        else:
                if initial:
                        need_fixing.append([s, filename, trait])
                return False
          
def check_traits(filename):
        f = os.path.join(directory, filename)
        if check_if_audio(f):
                s = music_tag.load_file(filename)
                for trait in relevant_traits:
                        if s[trait]:
                                pass
                        else:
                                autofix(s, filename, trait, True)
                                if s[trait]:
                                        pass


def manual_fix():
        for item in need_fixing:
                if autofix(item[0], item[1], item[2], False):
                        pass
                else:
                        manual_trait = ''
                        given_name = ''
                        if item[0]['title']:
                                given_name = str(item[0]['title'])
                        else:
                                given_name = str(item[1])
                        manual_trait = input((given_name + ' is missing ' + str(item[2]) + '. Enter manually: '))    
                        item[0][item[2]] = manual_trait
                        item[0].save()   

#autofix(music_tag.load_file(r'c:\Users\micro\Music\my-music\music\artists\g-jones\acid-disk\03-help!-i-cant-find-my-way-out.wav'), '03-help!-i-cant-find-my-way-out.wav', 'tracknumber')
for filename in os.listdir(directory):
        check_traits(filename)  
manual_fix()
                           
                                

