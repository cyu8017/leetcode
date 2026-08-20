// LeetCode 2517 - Maximum Tastiness of Candy Basket
// https://leetcode.com/problems/maximum-tastiness-of-candy-basket/

import "sort"

func maximumTastiness(price []int, k int) int {
	sort.Ints(price)
	ok := func(d int) bool {
		cnt, last := 1, price[0]
		for i := 1; i < len(price); i++ {
			if price[i]-last >= d {
				cnt++
				last = price[i]
				if cnt >= k {
					return true
				}
			}
		}
		return false
	}
	lo, hi := 0, price[len(price)-1]-price[0]
	for lo < hi {
		mid := (lo + hi + 1) / 2
		if ok(mid) {
			lo = mid
		} else {
			hi = mid - 1
		}
	}
	return lo
}
