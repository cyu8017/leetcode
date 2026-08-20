// LeetCode 2234 - Maximum Total Beauty of the Gardens
// https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/

import "sort"

func maximumBeauty(flowers []int, newFlowers int64, target int, full int, partial int) int64 {
	n := len(flowers)
	for i := range flowers {
		if flowers[i] > target {
			flowers[i] = target
		}
	}
	sort.Ints(flowers)
	var sum int64
	for _, f := range flowers {
		sum += int64(f)
	}
	if int64(target)*int64(n)-sum <= newFlowers {
		return int64(n) * int64(full)
	}
	pref := make([]int64, n+1)
	for i := 0; i < n; i++ {
		pref[i+1] = pref[i] + int64(flowers[i])
	}
	ans := int64(0)
	j := n - 1
	remain := newFlowers
	for complete := 0; complete <= n; complete++ {
		if complete > 0 {
			need := int64(target - flowers[n-complete])
			if remain < need {
				break
			}
			remain -= need
		}
		for j >= n-complete || (j >= 0 && int64(flowers[j])*int64(j+1)-pref[j+1] > remain) {
			j--
		}
		var partialVal int64
		if j >= 0 {
			extra := (remain - (int64(flowers[j])*int64(j+1) - pref[j+1])) / int64(j+1)
			partialVal = int64(flowers[j]) + extra
			if partialVal >= int64(target) {
				partialVal = int64(target) - 1
			}
		}
		cand := int64(complete)*int64(full) + partialVal*int64(partial)
		if cand > ans {
			ans = cand
		}
	}
	return ans
}
