// LeetCode 3410 - Maximize Subarray Sum After Removing All Occurrences of One Element
// https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/

func maxSubarraySum(nums []int) int64 {
	n := len(nums)
	var kadane func([]int) int64
	kadane = func(a []int) int64 {
		var best, cur int64 = int64(-1 << 62), 0
		for _, x := range a {
			cur += int64(x)
			if cur > best {
				best = cur
			}
			if cur < 0 {
				cur = 0
			}
		}
		// if all negative
		allNeg := true
		var mx int64 = int64(a[0])
		for _, x := range a {
			if int64(x) > mx {
				mx = int64(x)
			}
			if x >= 0 {
				allNeg = false
			}
		}
		if allNeg {
			return mx
		}
		return best
	}
	ans := kadane(nums)
	uniq := map[int]bool{}
	for _, x := range nums {
		if x < 0 {
			uniq[x] = true
		}
	}
	for v := range uniq {
		b := make([]int, 0, n)
		for _, x := range nums {
			if x != v {
				b = append(b, x)
			}
		}
		if len(b) == 0 {
			continue
		}
		cand := kadane(b)
		if cand > ans {
			ans = cand
		}
	}
	return ans
}
