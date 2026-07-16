// LeetCode 0255 - Verify Preorder Sequence in Binary Search Tree
// https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/

func verifyPreorder(preorder []int) bool {
	low := int(^uint(0) >> 1)
	low = -low - 1
	stack := make([]int, 0)

	for _, value := range preorder {
		if value < low {
			return false
		}
		for len(stack) > 0 && stack[len(stack)-1] < value {
			low = stack[len(stack)-1]
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, value)
	}

	return true
}
