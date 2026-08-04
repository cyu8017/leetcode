// LeetCode 1191 - K-Concatenation Maximum Sum
// https://leetcode.com/problems/k-concatenation-maximum-sum/

func kConcatenationMaxSum(arr []int, k int) int {
	const MOD = 1000000007
	kadane := func(nums []int) int {
		best, cur := 0, 0
		for _, x := range nums {
			cur += x
			if cur < 0 {
				cur = 0
			}
			if cur > best {
				best = cur
			}
		}
		return best
	}
	one := kadane(arr)
	if k == 1 {
		return one % MOD
	}
	twoArr := append(append([]int{}, arr...), arr...)
	two := kadane(twoArr)
	total := 0
	for _, x := range arr {
		total += x
	}
	ans := one
	if two > ans {
		ans = two
	}
	if total > 0 {
		cand := two + total*(k-2)
		if cand > ans {
			ans = cand
		}
	}
	return ans % MOD
}
