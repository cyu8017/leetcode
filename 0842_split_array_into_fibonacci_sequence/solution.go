// LeetCode 0842 - Split Array into Fibonacci Sequence
// https://leetcode.com/problems/split-array-into-fibonacci-sequence/

func splitIntoFibonacci(num string) []int {
	n := len(num)
	path := []int{}
	var dfs func(int) bool
	dfs = func(start int) bool {
		if start == n {
			return len(path) >= 3
		}
		for end := start; end < n; end++ {
			if num[start] == '0' && end > start {
				break
			}
			val := 0
			ok := true
			for i := start; i <= end; i++ {
				val = val*10 + int(num[i]-'0')
				if val > 1<<31-1 {
					ok = false
					break
				}
			}
			if !ok {
				break
			}
			if len(path) >= 2 {
				total := path[len(path)-1] + path[len(path)-2]
				if val < total {
					continue
				}
				if val > total {
					break
				}
			}
			path = append(path, val)
			if dfs(end + 1) {
				return true
			}
			path = path[:len(path)-1]
		}
		return false
	}
	dfs(0)
	return path
}
