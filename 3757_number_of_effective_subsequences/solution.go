// LeetCode 3757 - Number of Effective Subsequences
// https://leetcode.com/problems/number-of-effective-subsequences/

func countEffectiveSubsequences(nums []int) int {
	const mod = 1000000007
	all := 0
	for _, x := range nums {
		all |= x
	}
	bits := make([]int, 0)
	for b := 0; b < 20; b++ {
		if all>>b&1 != 0 {
			bits = append(bits, b)
		}
	}
	m := len(bits)
	freq := make([]int, 1<<m)
	for _, x := range nums {
		mask := 0
		for i, b := range bits {
			if x>>b&1 != 0 {
				mask |= 1 << i
			}
		}
		freq[mask]++
	}
	disjoint := append([]int(nil), freq...)
	for b := 0; b < m; b++ {
		for mask := 0; mask < 1<<m; mask++ {
			if mask>>b&1 != 0 {
				disjoint[mask] += disjoint[mask^(1<<b)]
			}
		}
	}
	pow2 := make([]int, len(nums)+1)
	pow2[0] = 1
	for i := 1; i <= len(nums); i++ {
		pow2[i] = pow2[i-1] * 2 % mod
	}
	ans, full := 0, (1<<m)-1
	for s := 1; s <= full; s++ {
		ways := pow2[disjoint[full^s]]
		if bitCount3757(s)&1 == 1 {
			ans += ways
			if ans >= mod {
				ans -= mod
			}
		} else {
			ans -= ways
			if ans < 0 {
				ans += mod
			}
		}
	}
	return ans
}

func bitCount3757(x int) int {
	res := 0
	for x != 0 {
		x &= x - 1
		res++
	}
	return res
}