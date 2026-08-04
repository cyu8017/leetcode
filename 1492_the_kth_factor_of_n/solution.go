// LeetCode 1492 - The kth Factor of n
// https://leetcode.com/problems/the-kth-factor-of-n/

func kthFactor(n int, k int) int {
	for x := 1; x <= n; x++ {
		if n%x == 0 {
			k--
			if k == 0 {
				return x
			}
		}
	}
	return -1
}
