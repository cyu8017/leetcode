// LeetCode 1237 - Find Positive Integer Solution for a Given Equation
// https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

type CustomFunction interface {
	f(x int, y int) int
}

func findSolution(customfunction CustomFunction, z int) [][]int {
	ans := [][]int{}
	x, y := 1, 1000
	for x <= 1000 && y >= 1 {
		value := customfunction.f(x, y)
		if value == z {
			ans = append(ans, []int{x, y})
			x++
			y--
		} else if value < z {
			x++
		} else {
			y--
		}
	}
	return ans
}
