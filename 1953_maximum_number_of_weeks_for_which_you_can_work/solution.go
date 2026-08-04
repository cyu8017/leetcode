// LeetCode 1953 - Maximum Number of Weeks for Which You Can Work
// https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/

func numberOfWeeks(milestones []int) int64 {
	var total int64
	mx := 0
	for _, m := range milestones {
		total += int64(m)
		if m > mx {
			mx = m
		}
	}
	rest := total - int64(mx)
	if int64(mx) > rest+1 {
		return 2*rest + 1
	}
	return total
}
