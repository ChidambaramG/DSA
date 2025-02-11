#Keep two separate counters for word and abbreviations and make sure of the limits.
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        abbr_counter = 0
        word_counter = 0
        while(abbr_counter < len(abbr) and word_counter < len(word)):
            print(word[word_counter], word_counter, abbr[abbr_counter], abbr_counter)
            if abbr[abbr_counter] == word[word_counter]:
                abbr_counter += 1
                word_counter += 1
            else:
                if not abbr[abbr_counter].isdigit():
                    return False
                if abbr[abbr_counter] == '0':
                    return False
                else:
                    temp = ""
                    for j in range(abbr_counter, len(abbr)):
                        if abbr[j].isdigit():
                            temp += abbr[j]
                        else:
                            break
                    temp_int = int(temp)
                    print(temp_int)
                    if temp_int == 1:
                        word_counter += temp_int
                        abbr_counter += len(temp)
                    elif temp_int + word_counter > len(word):
                        return False
                    else:
                        word_counter += temp_int
                        abbr_counter += len(temp)
        print(word_counter, abbr_counter)
        if word_counter == len(word) and abbr_counter == len(abbr):
            return True
        return False
        
