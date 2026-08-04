// LeetCode 1577 - Number of Ways Where Square of Number Is Equal to Product of Two Numbers
// https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/

func numTriplets(nums1 []int, nums2 []int) int {
	count := func(a, b []int) int {
		squares := map[int]int{}
		for _, x := range a {
			squares[x*x]++
		}
		products := map[int]int{}
		for i := 0; i < len(b); i++ {
			for j := i + 1; j < len(b); j++ {
				products[b[i]*b[j]]++
			}
		}
		ans := 0
		for value, c := range squares {
			ans += c * products[value]
		}
		return ans
	}
	return count(nums1, nums2) + count(nums2, nums1)
}
