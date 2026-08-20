// LeetCode 2640 - Find the Score of All Prefixes of an Array
// https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/


func findPrefixScore(nums []int) []int64 {
	ans := make([]int64, len(nums))
	mx := 0
	var sum int64
	for i, x := range nums {
		if x > mx {
			mx = x
		}
		sum += int64(x + mx)
		ans[i] = sum
	}
	return ans
}
