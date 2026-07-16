// LeetCode 0523 - Continuous Subarray Sum
// https://leetcode.com/problems/continuous-subarray-sum/

func checkSubarraySum(nums []int, k int) bool {
	prefix := 0
	remainders := map[int]int{0: -1}

	for index, num := range nums {
		prefix += num
		mod := prefix
		if k != 0 {
			mod = prefix % k
		}
		if prev, ok := remainders[mod]; ok {
			if index-prev >= 2 {
				return true
			}
		} else {
			remainders[mod] = index
		}
	}
	return false
}
