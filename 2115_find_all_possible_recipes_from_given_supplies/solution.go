// LeetCode 2115 - Find All Possible Recipes from Given Supplies
// https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

func findAllRecipes(recipes []string, ingredients [][]string, supplies []string) []string {
	have := map[string]bool{}
	for _, s := range supplies {
		have[s] = true
	}
	indeg := map[string]int{}
	graph := map[string][]string{}
	recSet := map[string]bool{}
	for i, r := range recipes {
		recSet[r] = true
		indeg[r] = len(ingredients[i])
		for _, ing := range ingredients[i] {
			graph[ing] = append(graph[ing], r)
		}
	}
	q := []string{}
	for s := range have {
		q = append(q, s)
	}
	ans := []string{}
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		for _, nxt := range graph[cur] {
			indeg[nxt]--
			if indeg[nxt] == 0 {
				ans = append(ans, nxt)
				q = append(q, nxt)
			}
		}
	}
	return ans
}
