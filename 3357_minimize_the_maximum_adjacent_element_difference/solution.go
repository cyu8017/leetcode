// LeetCode 3357 - Minimize the Maximum Adjacent Element Difference
// https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/

func minDifference(nums []int) int {
	n := len(nums)
	ok := func(d int) bool {
		// assign -1 values so adjacent diff <= d
		prev := -1
		for i := 0; i < n; i++ {
			if nums[i] != -1 {
				if prev != -1 && abs3357(nums[i]-prev) > d {
					return false
				}
				prev = nums[i]
				continue
			}
			// gap of -1s
			j := i
			for j < n && nums[j] == -1 {
				j++
			}
			left := prev
			right := -1
			if j < n {
				right = nums[j]
			}
			gap := j - i
			if left == -1 && right == -1 {
				return true
			}
			if left == -1 || right == -1 {
				// can always fill with free choice near known
				prev = -1
				i = j - 1
				continue
			}
			if abs3357(left-right) > d*int(gap+1) {
				return false
			}
			prev = -1
			i = j - 1
		}
		return true
	}
	lo, hi := 0, int(1e9)
	for lo < hi {
		mid := (lo + hi) / 2
		if ok(mid) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}

func abs3357(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
