// LeetCode 1248 - Count Number of Nice Subarrays
// https://leetcode.com/problems/count-number-of-nice-subarrays/

func numberOfSubarrays(nums []int, k int) int {
	frequency := map[int]int{0: 1}
	odd, answer := 0, 0
	for _, x := range nums {
		odd += x & 1
		answer += frequency[odd-k]
		frequency[odd]++
	}
	return answer
}
