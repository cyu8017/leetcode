// LeetCode 3792 - Sum Of Increasing Product Blocks
// https://leetcode.com/problems/sum-of-increasing-product-blocks/

func sumOfBlocks(n int) (ans int) {
	const mod int = 1e9 + 7
	k := 1
	for i := 1; i <= n; i++ {
		x := 1
		for j := k; j < k+i; j++ {
			x = x * j % mod
		}
		ans = (ans + x) % mod
		k += i
	}
	return
}
