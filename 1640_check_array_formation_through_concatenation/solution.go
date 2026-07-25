// LeetCode 1640 - Check Array Formation Through Concatenation
// https://leetcode.com/problems/check-array-formation-through-concatenation/

func canFormArray(arr []int, pieces [][]int) bool {
	byFirst := map[int][]int{}
	for _, p := range pieces {
		byFirst[p[0]] = p
	}
	i := 0
	for i < len(arr) {
		p, ok := byFirst[arr[i]]
		if !ok {
			return false
		}
		for _, v := range p {
			if i >= len(arr) || arr[i] != v {
				return false
			}
			i++
		}
	}
	return true
}
