// LeetCode 3366 - Minimum Array Sum
// https://leetcode.com/problems/minimum-array-sum/

func minArraySum(nums []int, k int, op1 int, op2 int) int {
	n := len(nums)
	const inf = int(1e18)
	// dp[i][o1][o2] too big; n<=100, op1,op2<=100
	dp := make([][]int, op1+1)
	for i := range dp {
		dp[i] = make([]int, op2+1)
		for j := range dp[i] {
			dp[i][j] = inf
		}
	}
	dp[0][0] = 0
	for _, x := range nums {
		ndp := make([][]int, op1+1)
		for i := range ndp {
			ndp[i] = make([]int, op2+1)
			for j := range ndp[i] {
				ndp[i][j] = inf
			}
		}
		for a := 0; a <= op1; a++ {
			for b := 0; b <= op2; b++ {
				if dp[a][b] == inf {
					continue
				}
				// no op
				cand := []struct{ na, nb, v int }{{a, b, x}}
				if a < op1 {
					cand = append(cand, struct{ na, nb, v int }{a + 1, b, (x + 1) / 2})
				}
				if b < op2 && x >= k {
					cand = append(cand, struct{ na, nb, v int }{a, b + 1, x - k})
				}
				if a < op1 && b < op2 {
					// both orders
					v1 := (x + 1) / 2
					if v1 >= k {
						cand = append(cand, struct{ na, nb, v int }{a + 1, b + 1, v1 - k})
					}
					if x >= k {
						v2 := (x - k + 1) / 2
						cand = append(cand, struct{ na, nb, v int }{a + 1, b + 1, v2})
					}
				}
				for _, c := range cand {
					if dp[a][b]+c.v < ndp[c.na][c.nb] {
						ndp[c.na][c.nb] = dp[a][b] + c.v
					}
				}
			}
		}
		dp = ndp
		_ = n
	}
	ans := inf
	for a := 0; a <= op1; a++ {
		for b := 0; b <= op2; b++ {
			if dp[a][b] < ans {
				ans = dp[a][b]
			}
		}
	}
	return ans
}
