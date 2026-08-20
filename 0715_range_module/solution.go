// LeetCode 0715 - Range Module
// https://leetcode.com/problems/range-module/

type RangeModule struct {
	intervals [][]int
}

func Constructor() RangeModule {
	return RangeModule{}
}

func (this *RangeModule) AddRange(left int, right int) {
	newIntervals := [][]int{}
	placed := false
	for _, iv := range this.intervals {
		start, end := iv[0], iv[1]
		if end < left {
			newIntervals = append(newIntervals, []int{start, end})
		} else if right < start {
			if !placed {
				newIntervals = append(newIntervals, []int{left, right})
				placed = true
			}
			newIntervals = append(newIntervals, []int{start, end})
		} else {
			if start < left {
				left = start
			}
			if end > right {
				right = end
			}
		}
	}
	if !placed {
		newIntervals = append(newIntervals, []int{left, right})
	}
	this.intervals = newIntervals
}

func (this *RangeModule) QueryRange(left int, right int) bool {
	lo, hi := 0, len(this.intervals)
	for lo < hi {
		mid := (lo + hi) / 2
		if this.intervals[mid][0] <= left {
			lo = mid + 1
		} else {
			hi = mid
		}
	}
	i := lo - 1
	if i < 0 {
		return false
	}
	return this.intervals[i][0] <= left && right <= this.intervals[i][1]
}

func (this *RangeModule) RemoveRange(left int, right int) {
	newIntervals := [][]int{}
	for _, iv := range this.intervals {
		start, end := iv[0], iv[1]
		if end <= left || right <= start {
			newIntervals = append(newIntervals, []int{start, end})
		} else {
			if start < left {
				newIntervals = append(newIntervals, []int{start, left})
			}
			if right < end {
				newIntervals = append(newIntervals, []int{right, end})
			}
		}
	}
	this.intervals = newIntervals
}
