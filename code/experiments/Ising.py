import sys
sys.path.append('./code')
from deepbelief import *
from numpy import *
from numpy.random import permutation

x = []
vals = []
data = []

def main(argv):
    num_visibles = 40 * 40
    num_hiddens = [1600,400,100,25]
    num_epochs = 200
    batch_size = 100
    ifile = open("./data/lattice.txt",'r')
    count = 0
    for rows in ifile:
        if(count == 1000):
            break
        rows.strip()
        for row in rows:
            if(row != ","):
                x.append(float(row))
        vals.append(x)
    
    data = numpy.array(values)
    print(data)
    
            
        
    
        
        

'''
	# train 1st layer
    dbn = DBN(RBM(num_visibles, num_hiddens[0]))
    dbn.train(data, num_epochs, batch_size)

	# train 2nd layer
    dbn.add_layer(RBM(num_hiddens[0], num_hiddens[1]))
    dbn.train(data, num_epochs, batch_size, [1E-1, 1E-2])
    

    return 0'''



if __name__ == '__main__':
	sys.exit(main(sys.argv))
