"""
Question 3 in recursion assignment
"""


def pascal(n: int, count=2, l=None):
    if l is None:
        l = [[1, 1], [1]]
    if count <= n:
        t = []
        t.append(1)
        for i in range(1, len(l[0])):
            t.append(l[0][i] + l[0][i - 1])
        t.append(1)
        l.insert(0, t)
        return pascal(n, count + 1, l)
    else:
        for i in range(len(l) - 1, 0, -1):
            print(' ' * i, end=' ')
            for j in l[i]:
                print(j, end=' ')
            print('')


pascal(8)

"""
                            1
                        1       1
                    1       2       1
                1       3       3       1
            1       4       6       4       1
        1       5       10      10      5       1    
    1       6       15      20      15      6       1          
1       7       21      35      35      21      7       1   
"""
