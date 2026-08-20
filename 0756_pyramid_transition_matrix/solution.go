// LeetCode 0756 - Pyramid Transition Matrix
// https://leetcode.com/problems/pyramid-transition-matrix/

func pyramidTransition(bottom string, allowed []string) bool {
	transitions := map[string][]byte{}
	for _, triple := range allowed {
		key := triple[:2]
		transitions[key] = append(transitions[key], triple[2])
	}
	memo := map[string]bool{}
	var dfs func(string) bool
	dfs = func(row string) bool {
		if len(row) == 1 {
			return true
		}
		if v, ok := memo[row]; ok {
			return v
		}
		options := make([][]byte, 0, len(row)-1)
		for i := 0; i < len(row)-1; i++ {
			choices := transitions[row[i:i+2]]
			if len(choices) == 0 {
				memo[row] = false
				return false
			}
			options = append(options, choices)
		}
		var build func(int, []byte) bool
		build = func(index int, path []byte) bool {
			if index == len(options) {
				return dfs(string(path))
			}
			for _, ch := range options[index] {
				path = append(path, ch)
				if build(index+1, path) {
					return true
				}
				path = path[:len(path)-1]
			}
			return false
		}
		ans := build(0, nil)
		memo[row] = ans
		return ans
	}
	return dfs(bottom)
}
