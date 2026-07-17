// LeetCode 1852 - Distinct Numbers in Each Subarray
// https://leetcode.com/problems/distinct-numbers-in-each-subarray/

func distinctNumbers(nums []int, k int) []int {
	counts := make(map[int]int)
	for index := 0; index < k; index++ {
		counts[nums[index]]++
	}

	result := []int{len(counts)}
	left := 0
	for right := k; right < len(nums); right++ {
		counts[nums[right]]++
		outgoing := nums[left]
		counts[outgoing]--
		if counts[outgoing] == 0 {
			delete(counts, outgoing)
		}
		left++
		result = append(result, len(counts))
	}

	return result
}
