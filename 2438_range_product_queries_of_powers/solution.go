// LeetCode 2438 - Range Product Queries of Powers
// https://leetcode.com/problems/range-product-queries-of-powers/

func productQueries(n int, queries [][]int) []int {
	const mod = 1000000007
	powers := []int{}
	for bit := 0; bit < 31; bit++ {
		if (n>>bit)&1 == 1 {
			powers = append(powers, 1<<bit)
		}
	}
	ans := make([]int, len(queries))
	for i, q := range queries {
		prod := 1
		for j := q[0]; j <= q[1]; j++ {
			prod = int(int64(prod) * int64(powers[j]) % mod)
		}
		ans[i] = prod
	}
	return ans
}
