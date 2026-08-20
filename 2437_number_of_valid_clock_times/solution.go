// LeetCode 2437 - Number of Valid Clock Times
// https://leetcode.com/problems/number-of-valid-clock-times/

func countTime(time string) int {
	ans := 0
	for h := 0; h < 24; h++ {
		for m := 0; m < 60; m++ {
			hs := []byte{byte('0' + h/10), byte('0' + h%10)}
			ms := []byte{byte('0' + m/10), byte('0' + m%10)}
			ok := true
			if time[0] != '?' && time[0] != hs[0] {
				ok = false
			}
			if time[1] != '?' && time[1] != hs[1] {
				ok = false
			}
			if time[3] != '?' && time[3] != ms[0] {
				ok = false
			}
			if time[4] != '?' && time[4] != ms[1] {
				ok = false
			}
			if ok {
				ans++
			}
		}
	}
	return ans
}
