// LeetCode 3361 - Shift Distance Between Two Strings
// https://leetcode.com/problems/shift-distance-between-two-strings/

func shiftDistance(s string, t string, nextCost []int, previousCost []int) int64 {
	var ans int64
	for i := 0; i < len(s); i++ {
		a, b := int(s[i]-'a'), int(t[i]-'a')
		if a == b {
			continue
		}
		// forward
		fwd := int64(0)
		for x := a; x != b; x = (x + 1) % 26 {
			fwd += int64(nextCost[x])
		}
		bwd := int64(0)
		for x := a; x != b; x = (x + 25) % 26 {
			bwd += int64(previousCost[x])
		}
		if fwd < bwd {
			ans += fwd
		} else {
			ans += bwd
		}
	}
	return ans
}
