// LeetCode 2162 - Minimum Cost to Set Cooking Time
// https://leetcode.com/problems/minimum-cost-to-set-cooking-time/

func minCostSetTime(startAt int, moveCost int, pushCost int, targetSeconds int) int {
	cost := func(mins, secs int) int {
		if mins < 0 || mins > 99 || secs < 0 || secs > 99 {
			return 1 << 30
		}
		s := ""
		if mins > 0 {
			s = itoa2162(mins) + sprintf02(secs)
		} else {
			s = itoa2162(secs)
		}
		cur := byte('0' + startAt)
		ans := 0
		for i := 0; i < len(s); i++ {
			if s[i] != cur {
				ans += moveCost
				cur = s[i]
			}
			ans += pushCost
		}
		return ans
	}
	mins, secs := targetSeconds/60, targetSeconds%60
	ans := cost(mins, secs)
	if mins > 0 {
		c2 := cost(mins-1, secs+60)
		if c2 < ans {
			ans = c2
		}
	}
	return ans
}

func itoa2162(x int) string {
	if x == 0 {
		return "0"
	}
	b := []byte{}
	for x > 0 {
		b = append([]byte{byte('0' + x%10)}, b...)
		x /= 10
	}
	return string(b)
}

func sprintf02(x int) string {
	return string([]byte{byte('0' + x/10), byte('0' + x%10)})
}
