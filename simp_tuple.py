def likelihood():
    likelihoods = (50,38,27,99,4)
    return min(likelihoods)

def run():
    print(f"Minimun likelihood of falling: {likelihood()}%")

if __name__=="__main__":
    run()