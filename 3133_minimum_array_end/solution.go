// LeetCode 3133 - Minimum Array End
// https://leetcode.com/problems/minimum-array-end/

func minEnd(n int, x int) (ans int64) {
	n--
	ans = int64(x)
	for i := 0; i < 31; i++ {
		if x>>i&1 == 0 {
			ans |= int64((n & 1) << i)
			n >>= 1
		}
	}
	ans |= int64(n) << 31
	return
}
