from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import numpy as np

def find_nn_cos(v, Wv, k=10):
    """Find nearest neighbors of a given word, by cosine similarity.
    
    Returns two parallel lists: indices of nearest neighbors, and 
    their cosine similarities. Both lists are in descending order, 
    and inclusive: so nns[0] should be the index of the input word, 
    nns[1] should be the index of the first nearest neighbor, and so on.
    
    You may find the following numpy functions useful:
      np.linalg.norm : take the l2-norm of a vector or matrix
      np.dot : dot product or matrix multiplication
      np.argsort : get indices sorted by element value,
        so np.argsort(numbers)[-5:] will return the top five elements
    
    Args:
      v: (d-dimensional vector) word vector of interest
      Wv: (V x d matrix) word embeddings
      k: (int) number of neighbors to return
    
    Returns (nns, ds), where:
      nns: (k-dimensional vector of int), row indices of nearest neighbors, 
        which may include the given word.
      ds: (k-dimensional vector of float), cosine similarity of each 
        neighbor in nns.
    """

    #### YOUR CODE HERE ####
    
    # v (100,) Wv (400003, 100)
    num = np.dot(Wv, v) #(400003,)
    
    v_norm = np.linalg.norm(v) #l2 norm of vector v
    vi_norm = np.linalg.norm(Wv,axis=1)  # l2 norm of vectors vi
    denom = v_norm * vi_norm
    
    sim = np.true_divide(num,denom)

    nns = np.argsort(-sim)[:k]
    
    ds = sim[nns,]
    
    return nns, ds


    #### END(YOUR CODE) ####


def analogy(vA, vB, vC, Wv, k=5):
    """Compute a linear analogy in vector space, as described in the async.

    Find the vector(s) that best answer "A is to B as C is to ___", returning 
    the top k candidates by cosine similarity.
    
    Args:
      vA: (d-dimensional vector) vector for word A
      vB: (d-dimensional vector) vector for word B
      vC: (d-dimensional vector) vector for word C
      Wv: (V x d matrix) word embeddings
      k: (int) number of neighbors to return

    Returns (nns, ds), where:
      nns: (k-dimensional vector of int), row indices of the top candidate 
        words.
      ds: (k-dimensional vector of float), cosine similarity of each 
        of the top candidate words.
    """
    #### YOUR CODE HERE ####
    vD = vC + vB - vA
    
    nns, ds = find_nn_cos(vD, Wv, k)
    
    return nns, ds

    #### END(YOUR CODE) ####
