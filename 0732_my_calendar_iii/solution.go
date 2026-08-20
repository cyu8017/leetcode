// LeetCode 0732 - My Calendar III
// https://leetcode.com/problems/my-calendar-iii/

import "sort"

type MyCalendarThree struct {
	delta map[int]int
}

func Constructor() MyCalendarThree {
	return MyCalendarThree{delta: map[int]int{}}
}

func (this *MyCalendarThree) Book(startTime int, endTime int) int {
	this.delta[startTime]++
	this.delta[endTime]--
	times := make([]int, 0, len(this.delta))
	for t := range this.delta {
		times = append(times, t)
	}
	sort.Ints(times)
	current, best := 0, 0
	for _, t := range times {
		current += this.delta[t]
		if current > best {
			best = current
		}
	}
	return best
}
