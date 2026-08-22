// LeetCode 3369 - Design an Array Statistics Tracker
// https://leetcode.com/problems/design-an-array-statistics-tracker/

import "container/heap"
import "sort"

type StatisticsTracker struct {
	arr []int
	sum int64
	freq map[int]int
	modeFreq int
	modes map[int]bool
}

func Constructor() StatisticsTracker {
	return StatisticsTracker{freq: map[int]int{}, modes: map[int]bool{}}
}

func (this *StatisticsTracker) AddNumber(num int) {
	this.arr = append(this.arr, num)
	this.sum += int64(num)
	this.freq[num]++
	f := this.freq[num]
	if f > this.modeFreq {
		this.modeFreq = f
		this.modes = map[int]bool{num: true}
	} else if f == this.modeFreq {
		this.modes[num] = true
	}
}

func (this *StatisticsTracker) RemoveFirst() {
	if len(this.arr) == 0 {
		return
	}
	num := this.arr[0]
	this.arr = this.arr[1:]
	this.sum -= int64(num)
	this.freq[num]--
	if this.freq[num] == 0 {
		delete(this.freq, num)
	}
	// rebuild mode
	this.modeFreq = 0
	this.modes = map[int]bool{}
	for v, f := range this.freq {
		if f > this.modeFreq {
			this.modeFreq = f
			this.modes = map[int]bool{v: true}
		} else if f == this.modeFreq {
			this.modes[v] = true
		}
	}
}

func (this *StatisticsTracker) GetMean() int {
	if len(this.arr) == 0 {
		return 0
	}
	return int(this.sum / int64(len(this.arr)))
}

func (this *StatisticsTracker) GetMedian() int {
	n := len(this.arr)
	tmp := append([]int(nil), this.arr...)
	sort.Ints(tmp)
	if n%2 == 1 {
		return tmp[n/2]
	}
	return tmp[n/2-1]
}

func (this *StatisticsTracker) GetMode() int {
	best := int(1e18)
	for v := range this.modes {
		if v < best {
			best = v
		}
	}
	if best == int(1e18) {
		return 0
	}
	return best
}

// silence unused imports
var _ = heap.Init
