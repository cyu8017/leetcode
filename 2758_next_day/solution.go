// LeetCode 2758 - Next Day
// https://leetcode.com/problems/next-day/

import "time"

func nextDay(date string) string {
	t, err := time.Parse("2006-01-02", date)
	if err != nil {
		return date
	}
	return t.AddDate(0, 0, 1).Format("2006-01-02")
}
