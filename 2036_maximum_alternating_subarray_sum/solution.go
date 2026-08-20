// LeetCode 2036 - Maximum Alternating Subarray Sum
// https://leetcode.com/problems/maximum-alternating-subarray-sum/

func maximumAlternatingSubarraySum(nums []int) int64 {
	ans := int64(-1 << 63)
	var even, odd int64
	for i, v := range nums {
		x := int64(v)
		if i%2 == 0 {
			even += x
		} else {
			if even-x > 0 {
				even = even - x
			} else {
				even = 0
			}
		}
		if even > ans {
			ans = even
		}
	}
	even = 0
	for i := 1; i < len(nums); i++ {
		x := int64(nums[i])
		if i%2 == 1 {
			odd += x
		} else {
			if odd-x > 0 {
				odd = odd - x
			} else {
				odd = 0
			}
		}
		if odd > ans {
			ans = odd
		}
	}
	_ = even
	return ans
}
