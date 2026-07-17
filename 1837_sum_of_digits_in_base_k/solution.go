// LeetCode 1837 - Sum of Digits in Base K
// https://leetcode.com/problems/sum-of-digits-in-base-k/

func sumBase(n int, k int) int {
	total := 0
	for n > 0 {
		total += n % k
		n /= k
	}
	return total
}
