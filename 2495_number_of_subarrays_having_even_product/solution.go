// LeetCode 2495 - Number of Subarrays Having Even Product
// https://leetcode.com/problems/number-of-subarrays-having-even-product/

func evenProduct(nums []int) int64 {
	n := int64(len(nums))
	total := n * (n + 1) / 2
	var oddLen, odd int64
	for _, x := range nums {
		if x%2 == 1 {
			odd++
			oddLen += odd
		} else {
			odd = 0
		}
	}
	return total - oddLen
}
