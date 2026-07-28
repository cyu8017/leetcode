// LeetCode 1055 - Shortest Way to Form String
// https://leetcode.com/problems/shortest-way-to-form-string/

func shortestWay(source string, target string) int {
	sourceSet := map[byte]bool{}
	for i := 0; i < len(source); i++ {
		sourceSet[source[i]] = true
	}
	for i := 0; i < len(target); i++ {
		if !sourceSet[target[i]] {
			return -1
		}
	}
	ans := 0
	i := 0
	n := len(target)
	for i < n {
		ans++
		for j := 0; j < len(source); j++ {
			if i < n && target[i] == source[j] {
				i++
			}
		}
	}
	return ans
}
