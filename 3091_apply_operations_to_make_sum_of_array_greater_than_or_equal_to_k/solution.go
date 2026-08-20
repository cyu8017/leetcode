// LeetCode 3091 - Apply Operations to Make Sum of Array Greater Than or Equal to k
// https://leetcode.com/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/

func minOperations(k int) int {
	ans := k
	for a := 0; a < k; a++ {
		x := a + 1
		b := (k+x-1)/x - 1
		ans = min(ans, a+b)
	}
	return ans
}
