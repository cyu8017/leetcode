// LeetCode 3494 - Find the Minimum Amount of Time to Brew Potions
// https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/

func minTime(skill []int, mana []int) int64 {
	n, m := len(skill), len(mana)
	done := make([]int64, n)
	for j := 0; j < m; j++ {
		var t int64
		for i := 0; i < n; i++ {
			if done[i] > t {
				t = done[i]
			}
			t += int64(skill[i]) * int64(mana[j])
			done[i] = t
		}
		for i := n - 2; i >= 0; i-- {
			done[i] = done[i+1] - int64(skill[i+1])*int64(mana[j])
		}
	}
	return done[n-1]
}
