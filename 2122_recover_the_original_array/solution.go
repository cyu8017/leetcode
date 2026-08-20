// LeetCode 2122 - Recover the Original Array
// https://leetcode.com/problems/recover-the-original-array/

import "sort"

func recoverArray(nums []int) []int {
	sort.Ints(nums)
	n := len(nums)
	for i := 1; i < n; i++ {
		diff := nums[i] - nums[0]
		if diff == 0 || diff%2 != 0 {
			continue
		}
		k := diff / 2
		used := make([]bool, n)
		used[0], used[i] = true, true
		ans := []int{(nums[0] + nums[i]) / 2}
		l, r := 0, i
		ok := true
		for len(ans) < n/2 {
			for l < n && used[l] {
				l++
			}
			if l == n {
				ok = false
				break
			}
			need := nums[l] + 2*k
			for r < n && (used[r] || nums[r] < need) {
				r++
			}
			if r == n || nums[r] != need {
				ok = false
				break
			}
			used[l], used[r] = true, true
			ans = append(ans, nums[l]+k)
		}
		if ok {
			return ans
		}
	}
	return nil
}
