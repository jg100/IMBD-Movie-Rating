class BOW:
    def __init__(self):
        self.bagOfWords = []
    
    # vec is a vector of words to add to the bagOfWords
    def add_wordVec(self, vec):
        document_tf = {}
        
        for word in vec:
            if word not in document_tf:
                document_tf[word] = 1
            else:
                document_tf[word] += 1
        
        self.bagOfWords.append(document_tf)

# aBag = BOW()
# aBag.add_wordVec(["hello","bye","bye"])
# for x in aBag.bagOfWords:
#     print(x)