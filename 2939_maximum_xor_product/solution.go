// LeetCode 2939 - Maximum Xor Product
// https://leetcode.com/problems/maximum-xor-product/

func maximumXorProduct(a int64, b int64, n int) int {
	const mod = 1_000_000_007
	for i := n - 1; i >= 0; i-- {
		bit := int64(1) << i
		abit := a & bit
		bbit := b & bit
		if abit == bbit {
			a |= bit
			b |= bit
		} else if a > b {
			b |= bit
			a &^= bit
		} else {
			a |= bit
			b &^= bit
		}
	}
	return int((a % mod) * (b % mod) % mod)
}
