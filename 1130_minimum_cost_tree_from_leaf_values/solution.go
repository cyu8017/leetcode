// LeetCode 1130 - Minimum Cost Tree From Leaf Values
// https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

func mctFromLeafValues(arr []int) int {
	stack := []int{int(^uint(0) >> 1)}
	ans := 0
	for _, x := range arr {
		for stack[len(stack)-1] <= x {
			mid := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			left := stack[len(stack)-1]
			if left < x {
				ans += mid * left
			} else {
				ans += mid * x
			}
		}
		stack = append(stack, x)
	}
	for len(stack) > 2 {
		mid := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		ans += mid * stack[len(stack)-1]
	}
	return ans
}
