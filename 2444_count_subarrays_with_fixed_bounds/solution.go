// LeetCode 2444 - Count Subarrays With Fixed Bounds
// https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

func countSubarrays(nums []int, minK int, maxK int) int64 {
	var ans int64
	imin, imax, ibad := -1, -1, -1
	for i, x := range nums {
		if x < minK || x > maxK {
			ibad = i
		}
		if x == minK {
			imin = i
		}
		if x == maxK {
			imax = i
		}
		bound := imin
		if imax < bound {
			bound = imax
		}
		if bound > ibad {
			ans += int64(bound - ibad)
		}
	}
	return ans
}
