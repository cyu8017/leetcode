// LeetCode 2861 - Maximum Number of Alloys
// https://leetcode.com/problems/maximum-number-of-alloys/

func maxNumberOfAlloys(n int, k int, budget int, composition [][]int, stock []int, cost []int) int {
	ok := func(machines int64) bool {
		for _, comp := range composition {
			var spend int64
			for i := 0; i < n; i++ {
				need := machines*int64(comp[i]) - int64(stock[i])
				if need > 0 {
					spend += need * int64(cost[i])
				}
			}
			if spend <= int64(budget) {
				return true
			}
		}
		return false
	}
	lo, hi, ans := int64(0), int64(budget)+int64(stock[0])+1, 0
	for i := 1; i < n; i++ {
		if int64(budget)+int64(stock[i])+1 > hi {
			hi = int64(budget) + int64(stock[i]) + 1
		}
	}
	hi = 1e9
	for lo <= hi {
		mid := (lo + hi) / 2
		if ok(mid) {
			ans = int(mid)
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}
	return ans
}
