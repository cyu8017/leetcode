// LeetCode 3354 - Make Array Elements Equal to Zero
// https://leetcode.com/problems/make-array-elements-equal-to-zero/

func countValidSelections(nums []int) int {
	n := len(nums)
	ans := 0
	for i := 0; i < n; i++ {
		if nums[i] != 0 {
			continue
		}
		for _, dir := range []int{-1, 1} {
			a := append([]int(nil), nums...)
			cur, d := i, dir
			for cur >= 0 && cur < n {
				if a[cur] == 0 {
					cur += d
				} else {
					a[cur]--
					d = -d
					cur += d
				}
			}
			ok := true
			for _, v := range a {
				if v != 0 {
					ok = false
					break
				}
			}
			if ok {
				ans++
			}
		}
	}
	return ans
}
