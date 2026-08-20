// LeetCode 2409 - Count Days Spent Together
// https://leetcode.com/problems/count-days-spent-together/

func countDaysTogether(arriveAlice string, leaveAlice string, arriveBob string, leaveBob string) int {
	days := []int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
	toDay := func(s string) int {
		m := int(s[0]-'0')*10 + int(s[1]-'0')
		d := int(s[3]-'0')*10 + int(s[4]-'0')
		res := d
		for i := 0; i < m-1; i++ {
			res += days[i]
		}
		return res
	}
	a1, a2 := toDay(arriveAlice), toDay(leaveAlice)
	b1, b2 := toDay(arriveBob), toDay(leaveBob)
	start := a1
	if b1 > start {
		start = b1
	}
	end := a2
	if b2 < end {
		end = b2
	}
	if end < start {
		return 0
	}
	return end - start + 1
}
