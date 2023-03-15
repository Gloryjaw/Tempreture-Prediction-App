import pickle
class mdl:
    def predict(self, x):
        pdt = 1.0076005494236566*x + 1.0076005494236566
        return pdt
modal = mdl()
pickle.dump(modal, open("webmodel.pkl", "wb"))