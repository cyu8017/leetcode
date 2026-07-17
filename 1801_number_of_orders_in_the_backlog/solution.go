// LeetCode 1801 - Number of Orders in the Backlog
// https://leetcode.com/problems/number-of-orders-in-the-backlog/

import "container/heap"

const mod1801 = 1000000007

type backlogOrder struct {
	price  int
	amount int
}

type buyHeap []backlogOrder

func (h buyHeap) Len() int            { return len(h) }
func (h buyHeap) Less(i, j int) bool  { return h[i].price > h[j].price }
func (h buyHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *buyHeap) Push(x interface{}) { *h = append(*h, x.(backlogOrder)) }
func (h *buyHeap) Pop() interface{} {
	old := *h
	n := len(old)
	value := old[n-1]
	*h = old[:n-1]
	return value
}

type sellHeap []backlogOrder

func (h sellHeap) Len() int            { return len(h) }
func (h sellHeap) Less(i, j int) bool  { return h[i].price < h[j].price }
func (h sellHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *sellHeap) Push(x interface{}) { *h = append(*h, x.(backlogOrder)) }
func (h *sellHeap) Pop() interface{} {
	old := *h
	n := len(old)
	value := old[n-1]
	*h = old[:n-1]
	return value
}

func getNumberOfBacklogOrders(orders [][]int) int {
	buy := buyHeap{}
	sell := sellHeap{}
	heap.Init(&buy)
	heap.Init(&sell)

	for _, order := range orders {
		price, amount, orderType := order[0], order[1], order[2]
		if orderType == 0 {
			heap.Push(&buy, backlogOrder{price: price, amount: amount})
		} else {
			heap.Push(&sell, backlogOrder{price: price, amount: amount})
		}

		for buy.Len() > 0 && sell.Len() > 0 && buy[0].price >= sell[0].price {
			buyPrice, buyAmount := buy[0].price, buy[0].amount
			sellPrice, sellAmount := sell[0].price, sell[0].amount
			matched := buyAmount
			if sellAmount < matched {
				matched = sellAmount
			}
			buyAmount -= matched
			sellAmount -= matched
			heap.Pop(&buy)
			heap.Pop(&sell)
			if buyAmount > 0 {
				heap.Push(&buy, backlogOrder{price: buyPrice, amount: buyAmount})
			}
			if sellAmount > 0 {
				heap.Push(&sell, backlogOrder{price: sellPrice, amount: sellAmount})
			}
		}
	}

	total := 0
	for _, order := range buy {
		total = (total + order.amount) % mod1801
	}
	for _, order := range sell {
		total = (total + order.amount) % mod1801
	}
	return total
}
