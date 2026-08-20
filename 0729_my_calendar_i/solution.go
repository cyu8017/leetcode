// LeetCode 0729 - My Calendar I
// https://leetcode.com/problems/my-calendar-i/

type MyCalendar struct {
	bookings [][2]int
}

func Constructor() MyCalendar {
	return MyCalendar{}
}

func (this *MyCalendar) Book(startTime int, endTime int) bool {
	for _, b := range this.bookings {
		if b[0] < endTime && startTime < b[1] {
			return false
		}
	}
	this.bookings = append(this.bookings, [2]int{startTime, endTime})
	return true
}
