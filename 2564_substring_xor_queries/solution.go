// LeetCode 2564 - Substring XOR Queries
// https://leetcode.com/problems/substring-xor-queries/


func substringXorQueries(s string, queries [][]int) [][]int {
	pos := map[int][2]int{}
	n := len(s)
	for i := 0; i < n; i++ {
		if s[i] == '0' {
			if _, ok := pos[0]; !ok {
				pos[0] = [2]int{i, i}
			}
			continue
		}
		val := 0
		for j := i; j < n && j < i+30; j++ {
			val = val*2 + int(s[j]-'0')
			if _, ok := pos[val]; !ok {
				pos[val] = [2]int{i, j}
			}
		}
	}
	ans := make([][]int, len(queries))
	for i, q := range queries {
		need := q[0] ^ q[1]
		if p, ok := pos[need]; ok {
			ans[i] = []int{p[0], p[1]}
		} else {
			ans[i] = []int{-1, -1}
		}
	}
	return ans
}
