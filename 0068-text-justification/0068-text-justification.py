class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        result,cur,num_letters = [],[],0

        for word in words:
            if num_letters + len(word) + len(cur) > maxWidth:
                for i in range(maxWidth - num_letters):
                    cur[i % (len(cur) -1 or 1)] +=' '
                result.append(''.join(cur))

                cur,num_letters = [],0

            cur += [word]
            num_letters += len(word)
        return result + [' '.join(cur).ljust(maxWidth)]