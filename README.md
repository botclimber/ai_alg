# ai_alg
ALGORITHM IMPLEMENTATION

## MAIN GOAL
 make this code as generic as possible. In order to do that we need to implement all kind of informend and non-informed search functions.

- GENERAL_SEARCH:
	``` 
	function GENERAL_SEARCH(problem, QUEUEING_FN) retorna solucao ou falha
		nodes := MAKE_QUEUE(MAKE_NODE(INITIAL_STATE(problem))) 
			loop
				if EMPTY?(nodes) then return falha
					node := REMOVE_FRONT(nodes)
				if STATE(node) = GOAL_TEST[problem] then return node
		
				new_nodes := EXPAND(node,OPERATORS(problem))
				nodes := QUEUEING_FN(nodes,new_nodes)
			end  
	```

- BAND-WITH SEARCH:
	``` 
		function BREADTH_FIRST_SEARCH(problem) 
			retorna	solucao ou falha
			return GENERAL_SEARCH(problem,ENQUEUE_AT_END)  
	```

- DEPTH-SEARCH:
	``` missing  ```

- BIDIRECTIONAL:
	``` missing ```

## algClass.py

This file is the core one, that have the class where we will write the needed methods.

## 8puzzle.py

In every example we will import the main class from core file (algClass.py) ``` from algClass import magicBox ``` and use the methods we need to solve the problem.

--------------------------------------------------------------------------------------------------------------
# FROM HERE WE CAN PUT SOME TASKS TO START ON!
###### example:
- [ ] FIRST
- [ ] SECOND

(it is optional ofc)
