// LeetCode 1306 - Jump Game III
// https://leetcode.com/problems/jump-game-iii/

func canReach(arr []int, start int) bool {
	stack := []int{start}
	seen := map[int]bool{}
	for len(stack) > 0 {
		i := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if seen[i] || i < 0 || i >= len(arr) {
			continue
		}
		if arr[i] == 0 {
			return true
		}
		seen[i] = true
		stack = append(stack, i-arr[i], i+arr[i])
	}
	return false
}
