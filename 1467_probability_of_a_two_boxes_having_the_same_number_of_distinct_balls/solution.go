// LeetCode 1467 - Probability of a Two Boxes Having the Same Number of Distinct Balls
// https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/

func getProbability(balls []int) float64 {
	half := 0
	for _, b := range balls {
		half += b
	}
	half /= 2
	comb := func(n, k int) float64 {
		if k < 0 || k > n {
			return 0
		}
		res := 1.0
		for i := 0; i < k; i++ {
			res *= float64(n - i)
			res /= float64(i + 1)
		}
		return res
	}
	var good, total float64
	var dfs func(i, left, dl int, ways float64)
	dfs = func(i, left, dl int, ways float64) {
		if i == len(balls) {
			if left == half {
				total += ways
				if dl == 0 {
					good += ways
				}
			}
			return
		}
		for x := 0; x <= balls[i]; x++ {
			if left+x <= half {
				delta := 0
				if x > 0 {
					delta++
				}
				if x < balls[i] {
					delta--
				}
				dfs(i+1, left+x, dl+delta, ways*comb(balls[i], x))
			}
		}
	}
	dfs(0, 0, 0, 1)
	return good / total
}
