// LeetCode 3827 - Count Monobit Integers
// https://leetcode.com/problems/count-monobit-integers/

func countMonobit(n int) (ans int) {
	ans = 1
	for i, x := 1, 1; x <= n; i++ {
		ans++
		x += (1 << i)
	}
	return
}
