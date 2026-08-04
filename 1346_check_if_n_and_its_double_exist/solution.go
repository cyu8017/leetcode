// LeetCode 1346 - Check If N and Its Double Exist
// https://leetcode.com/problems/check-if-n-and-its-double-exist/

func checkIfExist(arr []int) bool {
	seen := map[int]bool{}
	for _, value := range arr {
		if seen[2*value] || (value%2 == 0 && seen[value/2]) {
			return true
		}
		seen[value] = true
	}
	return false
}
