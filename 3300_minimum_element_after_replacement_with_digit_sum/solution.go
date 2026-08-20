// LeetCode 3300 - Minimum Element After Replacement With Digit Sum
// https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

func minElement(nums []int) int {
	ans := int(1e9)
	for _, x := range nums {
		s := 0
		for x > 0 {
			s += x % 10
			x /= 10
		}
		if s < ans {
			ans = s
		}
	}
	return ans
}
