// LeetCode 2777 - Date Range Generator
// https://leetcode.com/problems/date-range-generator/

import "time"

func dateRangeGenerator(start string, end string, step int) []string {
	t, err := time.Parse("2006-01-02", start)
	if err != nil {
		return nil
	}
	endT, err := time.Parse("2006-01-02", end)
	if err != nil {
		return nil
	}
	ans := []string{}
	for !t.After(endT) {
		ans = append(ans, t.Format("2006-01-02"))
		t = t.AddDate(0, 0, step)
	}
	return ans
}
