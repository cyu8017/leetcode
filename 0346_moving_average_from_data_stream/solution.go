// LeetCode 0346 - Moving Average from Data Stream
// https://leetcode.com/problems/moving-average-from-data-stream/

type MovingAverage struct {
	size   int
	values []int
	total  int
}

func Constructor(size int) MovingAverage {
	return MovingAverage{size: size}
}

func (this *MovingAverage) Next(val int) float64 {
	this.values = append(this.values, val)
	this.total += val
	if len(this.values) > this.size {
		this.total -= this.values[0]
		this.values = this.values[1:]
	}
	return float64(this.total) / float64(len(this.values))
}
