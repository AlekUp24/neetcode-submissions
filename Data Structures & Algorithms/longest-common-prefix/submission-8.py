class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:


        for i in range(len(strs[0])): # kazda litera w pierwszym slowie
            for word in strs:           #kazde slowo w zbiorze
                if i == len(word) or word[i] != strs[0][i]: 
#jesli slowo jest krótsze niz pierwsze LUB sprawdzana litera tego slowo rozni sie od litery w pierwszym slowie 
                    return word[:i] #zwroc pierwsze znaki tego innego slowa

        return strs[0]