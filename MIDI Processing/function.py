

import sys, os, midi, math, string, time
import datetime

pattern1 = midi.read_midifile('/Users/Tong_Li/Downloads/CantGetEnoughOfYourLove.mid')
pattern2 = midi.read_midifile('/Users/Tong_Li/Downloads/MarryYou.mid')
pattern3 = midi.read_midifile('/Users/Tong_Li/Downloads/HesaPirate.mid')
pattern4 = midi.read_midifile('/Users/Tong_Li/Downloads/Titantic.mid')
pattern5 = midi.read_midifile('/Users/Tong_Li/Downloads/PokerFace.mid')
pattern6 = midi.read_midifile('/Users/Tong_Li/Downloads/GangnamStyle.mid')


def check_number_of_tracks(pattern):
    tracks = [0 for track in pattern] 
    number_of_tracks=len(tracks)
    return number_of_tracks

################################################################################        
def verify_only_one_channel_within_one_track(pattern):
    only_one_channel_within_one_track=[]    
    for track in pattern:                
        channel_numbers_within_one_track=[]        
        ################################################################################
        for events in track:            
            if isinstance(events, midi.NoteEvent):
                channel_numbers_within_one_track.append(events.channel)
        ################################################################################        
        number_of_channel=len(set(channel_numbers_within_one_track))   
        if number_of_channel<2:
            only_one_channel_within_one_track.append("true")
        else:
            only_one_channel_within_one_track.append("false")                        
    if (len(set(only_one_channel_within_one_track))==1) and (list(set(only_one_channel_within_one_track))[0]=="true"):
        return True
    else:
        return False
################################################################################        


def find_number_of_top_tracks_within_one_midi(pattern, threshold):
    count_of_NoteEvent_list=[]
    
    ########################################################################
    for track in pattern:   
        i=0
        for events in track:            
            if isinstance(events, midi.NoteEvent):
                i=i+1
        count_of_NoteEvent_list.append(i)
    ########################################################################
    
    max_count=max(count_of_NoteEvent_list)
    margin=max_count*threshold    
    counts=sum(count >= margin for count in count_of_NoteEvent_list)
    return counts
 
    

def find_max_min_pitch(pattern):
    pitch_list=[]        
    for track in pattern:
        for events in track:
            if isinstance(events, midi.NoteEvent):                
                pitch=events.pitch
                pitch_list.append(pitch)                
    min_pitch=min(pitch_list)
    max_pitch=max(pitch_list)
    return min_pitch, max_pitch





















    
