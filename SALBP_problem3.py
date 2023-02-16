import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G= nx.DiGraph()


G.add_nodes_from([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
G.add_edges_from([(1, 5),(2, 6), (3, 7), (4, 7), (5, 8), (6, 8), (7 , 9), (8, 10), (8, 11), (9, 12), (9, 13)
, (9, 14), (10, 15), (11, 16), (12, 17), (13, 18), (14, 19), (15, 20), (16, 20), (17, 20), (18, 20), (19, 20)])
attrs = {1: {'task1': 3}, 2: {'task2': 1}, 3: {'task3': 1}, 4: {'task4': 2}, 5: {'task5': 2}, 6: {'task6': 2}, 7: {'task7': 4}, 8: {'task8': 5}, 9: {'task9': 1}
, 10: {'task10': 2}, 11: {'task11': 3}, 12: {'task12': 3}, 13: {'task13': 2}, 14: {'task14': 2}, 15: {'task15': 1}, 16: {'task16': 1}, 17: {'task17': 1}
, 18: {'task18': 3}, 19: {'task19': 2}, 20: {'task20': 1}}
nx.set_node_attributes(G,attrs)

"""
a = "3"
i= 3
print(G.nodes[i]["task"+a])
"""

nb_tasks =  20
nb_solutions =  10 

def creating_random_solutions():
    
    tab =[None]*nb_tasks
    tab2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    
    A = np.arange(nb_solutions*nb_tasks).reshape(nb_solutions, nb_tasks)

    for j in range(nb_solutions):    
       

        for i in range(nb_tasks):  
            tab[i] = random.choice(tab2)
            tab2.remove(tab[i])

        A[j] = tab
        tab2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    
    return A

def fun(tabb, i):

    tab = tabb

    for e in range(0, nb_tasks):     

                    if tab[e] in list(G.predecessors(tab[i])) and e>i:
                        a = tab[e]
                        tab[e] = tab[i]
                        tab[i] = a
                        tab  = fun(tab, i)  #recursive call

    return tab

def precedence_relations(Array):

    AV = np.arange(nb_solutions*nb_tasks).reshape(nb_solutions, nb_tasks)
   
    for j in range(nb_solutions):
        tab = Array[j]

        for i in range(nb_tasks):
           
            tab = fun(tab, i)
                    

        AV[j] = tab

    return AV

def cycle_time(Array, n_workstation):

    cycle_times = [None]*len(Array)
    c_init = 5
    nbw = 1
    
    n1_trie = 0
    n2_trie = 0
    
    """
    M_stations[0] = [0, 0]
    M_stations[1] = [0, 0]
    M_stations[2] = [0, 0]
    M_stations[3] = [0, 0]
    temp_tab = [0,0]
    """
    #for i in range(nb_solutions):
    for i in range(len(Array)):   

        tab = Array[i]
    
        while nbw != n_workstation :
         
            c = c_init
            
            for j in range(nb_tasks):
                
                a = tab[j]

                if(c >= G.nodes[a]["task"+str(a)]):
                    c = c - G.nodes[a]["task"+str(a)] 
                                                                                                                                                  
                    #print("task:",a," Opt : ",G.nodes[a]["task"+str(a)])

                else :
                    nbw = nbw + 1
                    c = c_init
                    c = c - G.nodes[a]["task"+str(a)]
            
            if nbw < n_workstation:
                
                cycle_times[i]  = c_init
                break

            if (nbw != n_workstation):
                c_init = c_init + 1
                c = c_init 
                nbw = 1                                                                                                   
            
            else :
                cycle_times[i]  = c_init
                c_init = 5

                
        nbw = 1    

    return cycle_times    

def ma_in():
    M = creating_random_solutions()
    #print(M)
    M2 = precedence_relations(M)
    #print(M2)
    #cycle_time(M2)

    return M2

def show_graph():
    nx.draw(G, with_labels=True, node_color='green')
    #plt.savefig("path_graph1.png")
    plt.show()

#print(G.nodes())
#print(G.edges())
#nx.draw(G, with_labels=True, node_color='green')
#plt.savefig("path_graph1.png")
#plt.show()