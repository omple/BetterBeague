class Searcher:
    words = []

    def __init__(self):
        file = open("NWL2020.txt", mode='r', encoding='utf-8-sig')
        lines = file.readlines()
        for i in lines:
            self.words.append(i.split(" ")[0])
        file.close()

    def return_dictionary(self):
        return self.words

    @staticmethod
    def uppercase_list(lower_list):
        return [i.upper() for i in lower_list]

    @staticmethod
    def score(word):
        score = 0
        for l in word:
            if l in "EAIONRTLSU":
                score += 1
            elif l in "DG":
                score += 2
            elif l in "BCMP":
                score += 3
            elif l in "FHVWY":
                score += 4
            elif l in "K":
                score += 5
            elif l in "JX":
                score += 8
            elif l in "QZ":
                score += 10
        return score

    def rank_words(self, letters=[]):
        words = self.words_only_contains(letters)
        score_word = []

        for word in words:
            score_word.append({"word": word, "score": self.score(word)})

        return score_word

    @staticmethod
    def must_include(word_list=[], letter=""):
        new_list = []
        for word in word_list:
            if letter not in word:
                continue
            new_list.append(word)
        return new_list

    @staticmethod
    def must_include_dict(list={}, letter=""):
        new_list = []
        for val in list:
            if letter not in val["word"]:
                continue
            new_list.append(val["word"])
        return new_list

    def words_only_contains(self, letters=[]):
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                    "U", "V", "W", "X", "Y", "Z"]
        negative_list = alphabet.copy()

        for l in letters:
            if l in negative_list:
                negative_list.remove(l)

        final_list = []

        for word in self.words:
            value = True

            for l in negative_list:
                if l in word:
                    value = False
                    break

            for l in letters:
                if not (letters.count(l) >= word.count(l)):
                    value = False
                    break

            if value:
                final_list.append(word)

        return final_list
