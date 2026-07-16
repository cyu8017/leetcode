// LeetCode 0484 - Find Permutation
// https://leetcode.com/problems/find-permutation/

func findPermutation(s string) []int {
	stack := []int{1}
	result := make([]int, 0, len(s)+1)
	for _, ch := range s {
		if ch == 'I' {
			for len(stack) > 0 {
				result = append(result, stack[len(stack)-1])
				stack = stack[:len(stack)-1]
			}
		}
		stack = append(stack, len(stack)+len(result)+1)
	}
	for len(stack) > 0 {
		result = append(result, stack[len(stack)-1])
		stack = stack[:len(stack)-1]
	}
	return result
}
