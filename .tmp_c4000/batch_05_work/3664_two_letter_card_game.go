// LeetCode 3664 - Two-Letter Card Game
// https://leetcode.com/problems/two-letter-card-game/

func score(cards []string, x byte) int {
	xx := 0
	left := make([]int, 26)
	right := make([]int, 26)
	for _, c := range cards {
		a, b := c[0], c[1]
		if a == x && b == x {
			xx++
		} else if a == x {
			left[b-'a']++
		} else if b == x {
			right[a-'a']++
		}
	}
	pairGroup := func(arr []int) (pairs, rem int) {
		total, mx := 0, 0
		for _, v := range arr {
			total += v
			if v > mx {
				mx = v
			}
		}
		pairs = total / 2
		if total-mx < pairs {
			pairs = total - mx
		}
		rem = total - 2*pairs
		return
	}
	lp, lr := pairGroup(left)
	rp, rr := pairGroup(right)
	ans := lp + rp
	rem := lr + rr
	use := xx
	if use > rem {
		use = rem
	}
	ans += use
	xx -= use
	ans += xx / 2
	return ans
}
