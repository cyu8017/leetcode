// LeetCode 1313 - Decompress Run-Length Encoded List
// https://leetcode.com/problems/decompress-run-length-encoded-list/

func decompressRLElist(nums []int) []int {
	var answer []int
	for i := 0; i < len(nums); i += 2 {
		for j := 0; j < nums[i]; j++ {
			answer = append(answer, nums[i+1])
		}
	}
	return answer
}
