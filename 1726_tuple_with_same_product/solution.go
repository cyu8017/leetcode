// LeetCode 1726 - Tuple with Same Product
// https://leetcode.com/problems/tuple-with-same-product/

func tupleSameProduct(nums []int) int {
	counts := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			counts[nums[i]*nums[j]]++
		}
	}
	result := 0
	for _, count := range counts {
		result += count * (count - 1) * 4
	}
	return result
}
