// LeetCode 2195 - Append K Integers With Minimal Sum
// https://leetcode.com/problems/append-k-integers-with-minimal-sum/

import "sort"

func minimalKSum(nums []int, k int) int64 {
	sort.Ints(nums)
	var ans int64
	prev := 0
	for _, x := range nums {
		if x <= prev {
			continue
		}
		start := prev + 1
		end := x - 1
		if start <= end {
			cnt := end - start + 1
			if cnt > k {
				end = start + k - 1
				cnt = k
			}
			ans += int64(start+end) * int64(cnt) / 2
			k -= cnt
			if k == 0 {
				return ans
			}
		}
		prev = x
	}
	start := prev + 1
	end := start + k - 1
	ans += int64(start+end) * int64(k) / 2
	return ans
}
