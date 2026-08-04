// LeetCode 1449 - Form Largest Integer With Digits That Add up to Target
// https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/

func largestNumber(cost []int, target int) string {
	dp := make([]*string, target+1)
	empty := ""
	dp[0] = &empty
	for total := 1; total <= target; total++ {
		var best *string
		for digit := 1; digit <= 9; digit++ {
			price := cost[digit-1]
			if total >= price && dp[total-price] != nil {
				candidate := string(byte('0'+digit)) + *dp[total-price]
				if best == nil || len(candidate) > len(*best) || (len(candidate) == len(*best) && candidate > *best) {
					c := candidate
					best = &c
				}
			}
		}
		dp[total] = best
	}
	if dp[target] == nil {
		return "0"
	}
	return *dp[target]
}
