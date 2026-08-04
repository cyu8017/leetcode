// LeetCode 1118 - Number of Days in a Month
// https://leetcode.com/problems/number-of-days-in-a-month/

func numberOfDays(year int, month int) int {
	days := []int{0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
	if month == 2 && isLeap(year) {
		return 29
	}
	return days[month]
}

func isLeap(year int) bool {
	return year%400 == 0 || (year%4 == 0 && year%100 != 0)
}
