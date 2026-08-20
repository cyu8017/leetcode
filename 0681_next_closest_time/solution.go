// LeetCode 0681 - Next Closest Time
// https://leetcode.com/problems/next-closest-time/

import "fmt"

func nextClosestTime(time string) string {
	digits := map[byte]bool{}
	for i := 0; i < len(time); i++ {
		if time[i] != ':' {
			digits[time[i]] = true
		}
	}
	hh := int(time[0]-'0')*10 + int(time[1]-'0')
	mm := int(time[3]-'0')*10 + int(time[4]-'0')
	start := hh*60 + mm
	for delta := 1; delta <= 24*60; delta++ {
		mins := (start + delta) % (24 * 60)
		h, m := mins/60, mins%60
		cand := fmt.Sprintf("%02d%02d", h, m)
		ok := true
		for i := 0; i < 4; i++ {
			if !digits[cand[i]] {
				ok = false
				break
			}
		}
		if ok {
			return fmt.Sprintf("%02d:%02d", h, m)
		}
	}
	return time
}
