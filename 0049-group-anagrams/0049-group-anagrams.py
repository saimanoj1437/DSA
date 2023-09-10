class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        dict = {}

        for word in strs:

            sortedword = "".join(sorted(word))
            
            if sortedword not in dict:
                dict[sortedword]  = [word]
                
            else:
                 dict[sortedword].append(word)

        result = []

        for items in dict.values():

            result.append(items)

        return result

