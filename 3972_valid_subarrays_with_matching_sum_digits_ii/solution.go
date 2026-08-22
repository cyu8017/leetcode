// LeetCode 3972 - Valid Subarrays With Matching Sum Digits II
// https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-ii/

import "sort"

func countValidSubarrays(nums []int, x int) int64 {
	byRemainder := make([][]int64, 10)
	byRemainder[0] = append(byRemainder[0], 0)
	var prefix, answer int64
	for _, value := range nums {
		prefix += int64(value)
		required := int((prefix-int64(x))%10 + 10) % 10
		values := byRemainder[required]
		for power := int64(1); int64(x)*power <= prefix; power *= 10 {
			low := int64(x) * power
			high := int64(x+1)*power - 1
			minPrefix, maxPrefix := prefix-high, prefix-low
			left := sort.Search(len(values), func(i int) bool { return values[i] >= minPrefix })
			right := sort.Search(len(values), func(i int) bool { return values[i] > maxPrefix })
			answer += int64(right - left)
			if power > prefix/10 {
				break
			}
		}
		remainder := int(prefix % 10)
		byRemainder[remainder] = append(byRemainder[remainder], prefix)
	}
	return answer
}