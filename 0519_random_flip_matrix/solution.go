// LeetCode 0519 - Random Flip Matrix
// https://leetcode.com/problems/random-flip-matrix/

type UniformFn func(float64, float64) float64

var uniform UniformFn = func(low, _ float64) float64 { return low }

func setUniform(uniformFn UniformFn) {
	uniform = uniformFn
}

func set_uniform(uniformFn UniformFn) {
	setUniform(uniformFn)
}

type Solution struct {
	cols      int
	total     int
	available []int
}

func Constructor(m int, n int) Solution {
	solution := Solution{
		cols:  n,
		total: m * n,
	}
	solution.resetAvailable()
	return solution
}

func (solution *Solution) resetAvailable() {
	solution.available = make([]int, solution.total)
	for index := 0; index < solution.total; index++ {
		solution.available[index] = index
	}
}

func (solution *Solution) Flip() []int {
	index := int(uniform(0, float64(len(solution.available)-1)))
	if index >= len(solution.available) {
		index = len(solution.available) - 1
	}
	value := solution.available[index]
	last := len(solution.available) - 1
	solution.available[index] = solution.available[last]
	solution.available = solution.available[:last]
	return []int{value / solution.cols, value % solution.cols}
}

func (solution *Solution) Reset() {
	solution.resetAvailable()
}
