#subset

def do_backtrack(a:list, inputs:list):
    c = []
    if (is_a_solution(a, inputs)):
        process_solution(a, inputs)
    else:
        construct_candidate(a, inputs, c)
        for i in c:
            a.append(i)
            do_backtrack(a, inputs)
            a.pop()
            
def is_a_solution(a:list, inputs:list)->bool:
    return len(a) == len(inputs)

def construct_candidate(a:list, inputs:list, c:list):
    c.append(True)
    c.append(False)

def process_solution(a:list, inputs:list):
    # print([inputs[i] for i, x in enumerate(a) if x])
    print([inputs[i] if x else '-' for i, x in enumerate(a)])
    
#do_backtrack([],['1','2'])

#----------------------------------------------------------------------------------------


#permutation
def do_backtrack(a:list, inputs:list):
    c = []
    if (is_a_solution(a, inputs)):
        process_solution(a, inputs)
    else:
        construct_candidate(a, inputs, c)
        for i in c:
            a.append(i)
            do_backtrack(a, inputs)
            a.pop()
            
def is_a_solution(a:list, inputs:list)->bool:
    return len(a) == len(inputs)

def construct_candidate(a:list, inputs:list, c:list):
    for i in inputs:
        if i not in a:
            c.append(i)

def process_solution(a:list, inputs:list):
    print(a)
    
do_backtrack([],[1, 2, 3, 4])
