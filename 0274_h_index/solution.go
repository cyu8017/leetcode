// LeetCode 0274 - H-Index
// https://leetcode.com/problems/h-index/

func hIndex(citations []int) int {
	buckets := make([]int, len(citations)+1)
	for _, citation := range citations {
		index := citation
		if index > len(citations) {
			index = len(citations)
		}
		buckets[index]++
	}
	total := 0
	for h := len(buckets) - 1; h >= 0; h-- {
		total += buckets[h]
		if total >= h {
			return h
		}
	}
	return 0
}
