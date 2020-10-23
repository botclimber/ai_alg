# ai_alg
ALGORITHM IMPLEMENTATION

## MAIN GOAL
 make this code as generic as possible. In order to do that we need to implement all kind of informend and non-informed search functions.

- GENERAL_SEARCH:
	``` function GENERAL_SEARCH(problem, QUEUEING_FN) retorna solucao ou falha
		nodes := MAKE_QUEUE(MAKE_NODE(INITIAL_STATE(problem))) 
			loop
				if EMPTY?(nodes) then return falha
					node := REMOVE_FRONT(nodes)
				if STATE(node) = GOAL_TEST[problem] then return node
		
				new_nodes := EXPAND(node,OPERATORS(problem))
				nodes := QUEUEING_FN(nodes,new_nodes)
			end  ```
