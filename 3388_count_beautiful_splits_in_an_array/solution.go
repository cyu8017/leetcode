// LeetCode 3388 - Count Beautiful Splits in an Array
// https://leetcode.com/problems/count-beautiful-splits-in-an-array/

func beautifulSplits(nums []int) int {
	n := len(nums)
	ans := 0
	for i := 1; i < n-1; i++ {
		for j := i + 1; j < n; j++ {
			// nums[0..i) is prefix of nums[i..j) OR nums[i..j) is prefix of nums[j..n)
			ok := false
			if i <= j-i && equal(nums[0:i], nums[i:i+i]) {
				ok = true
			}
			if !ok && j-i <= n-j && equal(nums[i:j], nums[j:j+(j-i)]) {
				ok = true
			}
			if ok {
				ans++
			}
		}
	}
	return ans
}

func equal(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}
