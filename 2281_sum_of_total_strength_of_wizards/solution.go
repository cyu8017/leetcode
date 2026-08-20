// LeetCode 2281 - Sum of Total Strength of Wizards
// https://leetcode.com/problems/sum-of-total-strength-of-wizards/

func totalStrength(strength []int) int {
	const mod = 1000000007
	n := len(strength)
	left := make([]int, n)
	right := make([]int, n)
	stack := []int{}
	for i := 0; i < n; i++ {
		for len(stack) > 0 && strength[stack[len(stack)-1]] >= strength[i] {
			stack = stack[:len(stack)-1]
		}
		if len(stack) == 0 {
			left[i] = -1
		} else {
			left[i] = stack[len(stack)-1]
		}
		stack = append(stack, i)
	}
	stack = stack[:0]
	for i := n - 1; i >= 0; i-- {
		for len(stack) > 0 && strength[stack[len(stack)-1]] > strength[i] {
			stack = stack[:len(stack)-1]
		}
		if len(stack) == 0 {
			right[i] = n
		} else {
			right[i] = stack[len(stack)-1]
		}
		stack = append(stack, i)
	}
	pref := make([]int64, n+1)
	prefPref := make([]int64, n+2)
	for i := 0; i < n; i++ {
		pref[i+1] = (pref[i] + int64(strength[i])) % mod
	}
	for i := 0; i <= n; i++ {
		prefPref[i+1] = (prefPref[i] + pref[i]) % mod
	}
	var ans int64
	for i := 0; i < n; i++ {
		l, r := left[i]+1, right[i]-1
		leftSum := (prefPref[i+1] - prefPref[l] + mod) % mod
		rightSum := (prefPref[r+2] - prefPref[i+1] + mod) % mod
		leftCnt := int64(i - l + 1)
		rightCnt := int64(r - i + 1)
		contrib := (rightCnt*leftSum%mod - leftCnt*rightSum%mod + mod) % mod
		ans = (ans + contrib*int64(strength[i])%mod) % mod
	}
	return int(ans)
}
