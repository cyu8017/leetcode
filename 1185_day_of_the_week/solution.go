// LeetCode 1185 - Day of the Week
// https://leetcode.com/problems/day-of-the-week/

func dayOfTheWeek(day int, month int, year int) string {
	// Sakamoto's methods
	t := []int{0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4}
	y := year
	if month < 3 {
		y--
	}
	w := (y + y/4 - y/100 + y/400 + t[month-1] + day) % 7
	days := []string{"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}
	return days[w]
}
