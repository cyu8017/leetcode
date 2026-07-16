// LeetCode 0278 - First Bad Version
// https://leetcode.com/problems/first-bad-version/

func isBadVersion(version int) bool {
	return false
}

func firstBadVersion(n int) int {
	left, right := 1, n
	for left < right {
		mid := left + (right-left)/2
		if isBadVersion(mid) {
			right = mid
		} else {
			left = mid + 1
		}
	}
	return left
}
