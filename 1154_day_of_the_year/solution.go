// LeetCode 1154 - Day of the Year
// https://leetcode.com/problems/day-of-the-year/

func dayOfYear(date string) int {
	year := atoi(date[0:4])
	month := atoi(date[5:7])
	day := atoi(date[8:10])
	leap := year%4 == 0 && (year%100 != 0 || year%400 == 0)
	days := []int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
	if leap {
		days[1] = 29
	}
	ans := day
	for i := 0; i < month-1; i++ {
		ans += days[i]
	}
	return ans
}

func atoi(s string) int {
	n := 0
	for i := 0; i < len(s); i++ {
		n = n*10 + int(s[i]-'0')
	}
	return n
}
