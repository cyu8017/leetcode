// LeetCode 1360 - Number of Days Between Two Dates
// https://leetcode.com/problems/number-of-days-between-two-dates/

import "time"

func daysBetweenDates(date1 string, date2 string) int {
	a, _ := time.Parse("2006-01-02", date1)
	b, _ := time.Parse("2006-01-02", date2)
	d := int(a.Sub(b).Hours() / 24)
	if d < 0 {
		return -d
	}
	return d
}
