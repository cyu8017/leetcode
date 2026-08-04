// LeetCode 1911 - Maximum Alternating Subsequence Sum
// https://leetcode.com/problems/maximum-alternating-subsequence-sum/

func maxAlternatingSum(nums []int) int64 {
	var even, odd int64
	for _, x := range nums {
		v := int64(x)
		ne := even
		if odd+v > ne {
			ne = odd + v
		}
		no := odd
		if even-v > no {
			no = even - v
		}
		even, odd = ne, no
	}
	return even
}
