// LeetCode 0868 - Binary Gap
// https://leetcode.com/problems/binary-gap/

func binaryGap(n int) int {
	last := -1
	ans := 0
	bit := 0
	for n > 0 {
		if n&1 == 1 {
			if last != -1 && bit-last > ans {
				ans = bit - last
			}
			last = bit
		}
		n >>= 1
		bit++
	}
	return ans
}
