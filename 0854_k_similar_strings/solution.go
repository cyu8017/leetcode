// LeetCode 0854 - K-Similar Strings
// https://leetcode.com/problems/k-similar-strings/

func kSimilarity(s1 string, s2 string) int {
	if s1 == s2 {
		return 0
	}
	target := s2
	type item struct {
		s    string
		dist int
	}
	queue := []item{{s1, 0}}
	seen := map[string]bool{s1: true}
	neighbors := func(s string) []string {
		arr := []byte(s)
		i := 0
		for arr[i] == target[i] {
			i++
		}
		res := []string{}
		for j := i + 1; j < len(arr); j++ {
			if arr[j] == target[i] && arr[j] != target[j] {
				arr[i], arr[j] = arr[j], arr[i]
				res = append(res, string(arr))
				arr[i], arr[j] = arr[j], arr[i]
			}
		}
		return res
	}
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		for _, nxt := range neighbors(cur.s) {
			if nxt == target {
				return cur.dist + 1
			}
			if !seen[nxt] {
				seen[nxt] = true
				queue = append(queue, item{nxt, cur.dist + 1})
			}
		}
	}
	return -1
}
