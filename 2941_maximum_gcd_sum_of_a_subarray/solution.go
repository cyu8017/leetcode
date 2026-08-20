// LeetCode 2941 - Maximum GCD-Sum of a Subarray
// https://leetcode.com/problems/maximum-gcd-sum-of-a-subarray/

func maxGcdSum(nums []int, k int) int64 {
	n := len(nums)
	pref := make([]int64, n+1)
	for i := 0; i < n; i++ {
		pref[i+1] = pref[i] + int64(nums[i])
	}
	var ans int64
	type pair struct{ g, idx int }
	st := []pair{}
	for i := 0; i < n; i++ {
		nst := []pair{{nums[i], i}}
		for _, p := range st {
			g := gcd(p.g, nums[i])
			if nst[len(nst)-1].g == g {
				continue
			}
			nst = append(nst, pair{g, p.idx})
		}
		st = nst
		for _, p := range st {
			if i-p.idx+1 >= k {
				cand := (pref[i+1] - pref[p.idx]) * int64(p.g)
				if cand > ans {
					ans = cand
				}
			}
		}
	}
	return ans
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
