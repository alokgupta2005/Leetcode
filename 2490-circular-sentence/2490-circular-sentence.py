class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()

        for i in range(len(words)):
            last_char = words[i][-1]
            next_char = words[(i + 1) % len(words)][0]

            if last_char != next_char:
                return False

        return True