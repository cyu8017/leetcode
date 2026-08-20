// LeetCode 2048 - Next Greater Numerically Balanced Number
// https://leetcode.com/problems/next-greater-numerically-balanced-number/

func nextBeautifulNumber(n int) int {
	balanced := func(x int) bool {
		cnt := [10]int{}
		for x > 0 {
			cnt[x%10]++
			x /= 10
		}
		for d := 0; d < 10; d++ {
			if cnt[d] > 0 && cnt[d] != d {
				return false
			}
		}
		return true
	}
	for x := n + 1; ; x++ {
		if balanced(x) {
			return x
		}
	}
}
