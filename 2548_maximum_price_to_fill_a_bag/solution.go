// LeetCode 2548 - Maximum Price to Fill a Bag
// https://leetcode.com/problems/maximum-price-to-fill-a-bag/


import sort
func maxPrice(items [][]int, capacity int) float64 {
	sort.Slice(items, func(i, j int) bool {
		return float64(items[i][0])/float64(items[i][1]) > float64(items[j][0])/float64(items[j][1])
	})
	ans := 0.0
	remain := capacity
	for _, it := range items {
		price, weight := it[0], it[1]
		if remain >= weight {
			ans += float64(price)
			remain -= weight
		} else {
			ans += float64(price) * float64(remain) / float64(weight)
			remain = 0
			break
		}
	}
	if remain > 0 {
		return -1
	}
	return ans
}
