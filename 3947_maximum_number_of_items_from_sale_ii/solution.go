// LeetCode 3947 - Maximum Number of Items From Sale II
// https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/

import "sort"

func maxItems(items [][]int, budget int) int {
	n := len(items)
	frequency := make([]int, n+1)
	minimumPrice := items[0][1]
	for _, item := range items {
		frequency[item[0]]++
		if item[1] < minimumPrice {
			minimumPrice = item[1]
		}
	}

	type batch struct {
		price int
		count int
	}
	batches := make([]batch, 0, n)
	for _, item := range items {
		gain := 0
		for multiple := item[0]; multiple <= n; multiple += item[0] {
			gain += frequency[multiple]
		}
		gain--
		if gain > 0 && item[1] < 2*minimumPrice {
			batches = append(batches, batch{item[1], gain})
		}
	}
	sort.Slice(batches, func(i, j int) bool {
		return batches[i].price < batches[j].price
	})

	remaining := int64(budget)
	answer := int64(budget / minimumPrice)
	var boosted int64
	for _, current := range batches {
		count := int64(current.count)
		affordable := remaining / int64(current.price)
		if affordable < count {
			count = affordable
		}
		remaining -= count * int64(current.price)
		boosted += count
		total := 2*boosted + remaining/int64(minimumPrice)
		if total > answer {
			answer = total
		}
		if count < int64(current.count) {
			break
		}
	}
	return int(answer)
}