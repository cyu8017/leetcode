// LeetCode 3871 - Count Commas In Range Ii
// https://leetcode.com/problems/count-commas-in-range-ii/

func countCommas(n int64) (ans int64) {
	for x := int64(1000); x <= n; x *= 1000 {
		ans += n - x + 1
	}
	return
}
