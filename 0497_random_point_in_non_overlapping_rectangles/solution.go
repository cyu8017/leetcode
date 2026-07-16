// LeetCode 0497 - Random Point in Non-overlapping Rectangles
// https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/

type UniformFn func(float64, float64) float64

var uniform UniformFn = func(low, _ float64) float64 { return low }

func setUniform(uniformFn UniformFn) {
	uniform = uniformFn
}

func set_uniform(uniformFn UniformFn) {
	setUniform(uniformFn)
}

type Solution struct {
	rects  [][]int
	prefix []int
	total  int
}

func Constructor(rects [][]int) Solution {
	solution := Solution{rects: rects}
	for _, rect := range rects {
		solution.total += (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1)
		solution.prefix = append(solution.prefix, solution.total)
	}
	return solution
}

func (solution *Solution) Pick() []int {
	index := int(uniform(0, float64(solution.total)))
	if index >= solution.total {
		index = solution.total - 1
	}

	lo, hi := 0, len(solution.prefix)-1
	for lo < hi {
		mid := lo + (hi-lo)/2
		if index < solution.prefix[mid] {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	if lo > 0 {
		index -= solution.prefix[lo-1]
	}

	rect := solution.rects[lo]
	width := rect[2] - rect[0] + 1
	return []int{rect[0] + index%width, rect[1] + index / width}
}
