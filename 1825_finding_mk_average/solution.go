// LeetCode 1825 - Finding MK Average
// https://leetcode.com/problems/finding-mk-average/

import "sort"

type MKAverage struct {
	m      int
	k      int
	stream []int
}

func Constructor(m int, k int) MKAverage {
	return MKAverage{m: m, k: k, stream: make([]int, 0)}
}

func (avg *MKAverage) AddElement(num int) {
	avg.stream = append(avg.stream, num)
}

func (avg *MKAverage) CalculateMKAverage() int {
	if len(avg.stream) < avg.m {
		return -1
	}
	window := make([]int, avg.m)
	copy(window, avg.stream[len(avg.stream)-avg.m:])
	sort.Ints(window)
	middle := window[avg.k : len(window)-avg.k]
	sum := 0
	for _, value := range middle {
		sum += value
	}
	return sum / len(middle)
}
