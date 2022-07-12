import re
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class ParseChords:
    def __init__(self) -> None:
        self.note_list = ["A", "B", "C", "D", "E", "F", "G"]
    
    def to_flat(self,note:str):
        if note == "A#":
            return "Gb"
        if note == "B#":
            return "C"
        if note == "E#":
            return "F"
        else:
            return self.post_process(self.note_list[self.note_list.index(note.replace("#","")) - 1] + "b")
    
    def post_process(self,note:str):
        if note == "A#":
            return "Ab"
        if note == "B#":
            return "Bb"
        if note == "E#":
            return "Eb"
        else:
            return note
    def to_sharp(self,note:str):
        if note == "Gb":
            return "A#"
        if note == "Cb":
            return "B"
        if note == "Fb":
            return "E"
        else:
            return self.post_process(self.note_list[self.note_list.index(note.replace("b","")) + 1] + "#")
            
    
    def convert_to_sharp(self,chord_string):
        
        for note in self.note_list:
            note = note + "b"
            chord_string = chord_string.replace(note,self.to_sharp(note))
        return chord_string

    def convert_to_flat(self,chord_string):
        for note in self.note_list:
            note = note + "#"
            chord_string = chord_string.replace(note,self.to_flat(note))
        return chord_string

if __name__ == "__main__":
    trial_string_sharp  = "A#maj7  C#maj7 D#maj7 F#maj7 G#maj7"
    trial_string_flat = "Abmaj7 Cbmaj7 Dbmaj7 Fbmaj7 Gbmaj7"
    parser = ParseChords()
    logger.info(f" Trial string in sharp {trial_string_sharp}")
    logger.info(f" Converted to Flat {parser.convert_to_flat(trial_string_sharp)}")
    logger.info(f" Trial string in flat {trial_string_flat}")
    logger.info(f" Converted to Sharp {parser.convert_to_sharp(trial_string_flat)}")

        
    
