// LeetCode 0731 - My Calendar II
// https://leetcode.com/problems/my-calendar-ii/

type MyCalendarTwo struct {
	booked   [][2]int
	overlaps [][2]int
}

func Constructor() MyCalendarTwo {
	return MyCalendarTwo{}
}

func (this *MyCalendarTwo) Book(startTime int, endTime int) bool {
	for _, o := range this.overlaps {
		if o[0] < endTime && startTime < o[1] {
			return false
		}
	}
	for _, b := range this.booked {
		if b[0] < endTime && startTime < b[1] {
			left := b[0]
			if startTime > left {
				left = startTime
			}
			right := b[1]
			if endTime < right {
				right = endTime
			}
			this.overlaps = append(this.overlaps, [2]int{left, right})
		}
	}
	this.booked = append(this.booked, [2]int{startTime, endTime})
	return true
}
