// LeetCode 0347 - Top K Frequent Elements
// https://leetcode.com/problems/top-k-frequent-elements/

func topKFrequent(nums []int, k int) []int {
	counts := make(map[int]int)
	for _, num := range nums {
		counts[num]++
	}

	buckets := make([][]int, len(nums)+1)
	for value, count := range counts {
		buckets[count] = append(buckets[count], value)
	}

	result := make([]int, 0, k)
	for index := len(buckets) - 1; index >= 0; index-- {
		for _, value := range buckets[index] {
			result = append(result, value)
			if len(result) == k {
				return result
			}
		}
	}

	return result
}
