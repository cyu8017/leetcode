// LeetCode 3411 - Maximum Subarray With Equal Products
// https://leetcode.com/problems/maximum-subarray-with-equal-products/

func maxLength(nums []int) int {
	n := len(nums)
	ans := 1
	for i := 0; i < n; i++ {
		prod, g, l := 1, 0, 1
		for j := i; j < n; j++ {
			if prod > 1e9/nums[j] {
				break
			}
			prod *= nums[j]
			if g == 0 {
				g = nums[j]
				l = nums[j]
			} else {
				g = gcd3411(g, nums[j])
				l = l / gcd3411(l, nums[j]) * nums[j]
			}
			if prod == l*g && j-i+1 > ans {
				ans = j - i + 1
			}
		}
	}
	return ans
}

func gcd3411(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
