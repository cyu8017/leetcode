// LeetCode 0478 - Generate Random Point in a Circle
// https://leetcode.com/problems/generate-random-point-in-a-circle/

import (
	"math"
	"math/rand"
)

var uniform = rand.Float64

func setUniform(uniformFn func() float64) {
	uniform = uniformFn
}

type Solution struct {
	radius   float64
	xCenter  float64
	yCenter  float64
}

func Constructor(radius float64, xCenter float64, yCenter float64) Solution {
	return Solution{
		radius:  radius,
		xCenter: xCenter,
		yCenter: yCenter,
	}
}

func sampleRange(low, high float64) float64 {
	return low + (high-low)*uniform()
}

func (solution *Solution) randPoint() []float64 {
	for {
		x := sampleRange(-solution.radius, solution.radius)
		y := sampleRange(-solution.radius, solution.radius)
		if x*x+y*y <= solution.radius*solution.radius {
			return []float64{
				math.Round((solution.xCenter+x)*100000) / 100000,
				math.Round((solution.yCenter+y)*100000) / 100000,
			}
		}
	}
}
