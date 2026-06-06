class Solution:
    def replaceWords(self, dictionary, sentence):
        roots = set(dictionary)
        words = sentence.split()

        for i in range(len(words)):
            for j in range(1, len(words[i]) + 1):
                prefix = words[i][:j]
                if prefix in roots:
                    words[i] = prefix
                    break

        return " ".join(words)