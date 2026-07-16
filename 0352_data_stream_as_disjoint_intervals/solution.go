// LeetCode 0352 - Data Stream as Disjoint Intervals
// https://leetcode.com/problems/data-stream-as-disjoint-intervals/

type SummaryRanges struct {
	intervals [][]int
}

func Constructor() SummaryRanges {
	return SummaryRanges{intervals: make([][]int, 0)}
}

func (this *SummaryRanges) AddNum(value int) {
	newInterval := []int{value, value}
	merged := make([][]int, 0)
	inserted := false

	for _, interval := range this.intervals {
		if interval[1] < value-1 {
			merged = append(merged, interval)
		} else if interval[0] > value+1 {
			if !inserted {
				merged = append(merged, newInterval)
				inserted = true
			}
			merged = append(merged, interval)
		} else {
			if interval[0] < newInterval[0] {
				newInterval[0] = interval[0]
			}
			if interval[1] > newInterval[1] {
				newInterval[1] = interval[1]
			}
		}
	}

	if !inserted {
		merged = append(merged, newInterval)
	}

	this.intervals = merged
}

func (this *SummaryRanges) GetIntervals() [][]int {
	return this.intervals
}
