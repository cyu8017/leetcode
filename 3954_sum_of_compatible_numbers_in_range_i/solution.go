// LeetCode 3954 - Sum Of Compatible Numbers In Range I
// https://leetcode.com/problems/sum-of-compatible-numbers-in-range-i/

func sumOfGoodIntegers(n int, k int) (ans int) {
	start := max(1, n-k)
	end := n + k
	for x := start; x <= end; x++ {
		if (n & x) == 0 {
			ans += x
		}
	}
	return
}
