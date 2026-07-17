// LeetCode 1871 - Jump Game VII
// https://leetcode.com/problems/jump-game-vii/

func canReach(s string, minJump int, maxJump int) bool {
	n := len(s)
	reachable := make([]bool, n)
	reachable[0] = true
	prefix := make([]int, n+1)

	for i := 0; i < n; i++ {
		if i > 0 && s[i] == '0' {
			left := i - maxJump
			if left < 0 {
				left = 0
			}
			right := i - minJump
			if right >= left && prefix[right+1]-prefix[left] > 0 {
				reachable[i] = true
			}
		}
		if reachable[i] {
			prefix[i+1] = prefix[i] + 1
		} else {
			prefix[i+1] = prefix[i]
		}
	}

	return reachable[n-1]
}
