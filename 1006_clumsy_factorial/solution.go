// LeetCode 1006 - Clumsy Factorial
// https://leetcode.com/problems/clumsy-factorial/

func clumsy(n int) int {
	stack := []int{n}
	n--
	op := 0
	for n > 0 {
		switch op % 4 {
		case 0:
			stack[len(stack)-1] *= n
		case 1:
			stack[len(stack)-1] /= n
		case 2:
			stack = append(stack, n)
		default:
			stack = append(stack, -n)
		}
		n--
		op++
	}
	sum := 0
	for _, x := range stack {
		sum += x
	}
	return sum
}
