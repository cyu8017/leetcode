// LeetCode 1477 - Find Two Non-overlapping Sub-arrays Each With Target Sum
// https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/

func minSumOfLengths(arr []int, target int) int {
	const inf = int(1e9)
	left, total, best, ans := 0, 0, inf, inf
	shortest := make([]int, len(arr))
	for i := range shortest {
		shortest[i] = inf
	}
	for right, x := range arr {
		total += x
		for total > target {
			total -= arr[left]
			left++
		}
		if total == target {
			length := right - left + 1
			if left > 0 && length+shortest[left-1] < ans {
				ans = length + shortest[left-1]
			}
			if length < best {
				best = length
			}
		}
		shortest[right] = best
	}
	if ans == inf {
		return -1
	}
	return ans
}
