// LeetCode 0528 - Random Pick with Weight
// https://leetcode.com/problems/random-pick-with-weight/

type UniformFn func(float64, float64) float64

var uniform UniformFn = func(low, _ float64) float64 { return low }

func setUniform(uniformFn UniformFn) {
	uniform = uniformFn
}

func set_uniform(uniformFn UniformFn) {
	setUniform(uniformFn)
}

type Solution struct {
	prefix []int
	total  int
}

func Constructor(w []int) Solution {
	prefix := make([]int, 0, len(w))
	total := 0
	for _, weight := range w {
		total += weight
		prefix = append(prefix, total)
	}
	return Solution{prefix: prefix, total: total}
}

func (solution *Solution) PickIndex() int {
	target := int(uniform(0, float64(solution.total)))
	if target >= solution.total {
		target = solution.total - 1
	}
	return bisectRight(solution.prefix, target)
}

func bisectRight(values []int, target int) int {
	low, high := 0, len(values)-1
	for low < high {
		mid := low + (high-low)/2
		if values[mid] <= target {
			low = mid + 1
		} else {
			high = mid
		}
	}
	return low
}
