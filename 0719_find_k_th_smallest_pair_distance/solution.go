// LeetCode 0719 - Find K-th Smallest Pair Distance
// https://leetcode.com/problems/find-k-th-smallest-pair-distance/

import "sort"

func smallestDistancePair(nums []int, k int) int {
	sort.Ints(nums)
	countPairs := func(distance int) int {
		count, left := 0, 0
		for right, value := range nums {
			for value-nums[left] > distance {
				left++
			}
			count += right - left
		}
		return count
	}
	lo, hi := 0, nums[len(nums)-1]-nums[0]
	for lo < hi {
		mid := (lo + hi) / 2
		if countPairs(mid) >= k {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}
