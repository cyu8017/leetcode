// LeetCode 2034 - Stock Price Fluctuation
// https://leetcode.com/problems/stock-price-fluctuation/

import "container/heap"

type pair2034 struct{ price, ts int }
type minH2034 []pair2034
type maxH2034 []pair2034

func (h minH2034) Len() int            { return len(h) }
func (h minH2034) Less(i, j int) bool  { return h[i].price < h[j].price }
func (h minH2034) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minH2034) Push(x interface{}) { *h = append(*h, x.(pair2034)) }
func (h *minH2034) Pop() interface{} {
	old := *h
	x := old[len(old)-1]
	*h = old[:len(old)-1]
	return x
}

func (h maxH2034) Len() int            { return len(h) }
func (h maxH2034) Less(i, j int) bool  { return h[i].price > h[j].price }
func (h maxH2034) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *maxH2034) Push(x interface{}) { *h = append(*h, x.(pair2034)) }
func (h *maxH2034) Pop() interface{} {
	old := *h
	x := old[len(old)-1]
	*h = old[:len(old)-1]
	return x
}

type StockPrice struct {
	latestTs int
	priceAt  map[int]int
	minHeap  minH2034
	maxHeap  maxH2034
}

func Constructor() StockPrice {
	return StockPrice{priceAt: map[int]int{}}
}

func (this *StockPrice) Update(timestamp int, price int) {
	this.priceAt[timestamp] = price
	if timestamp >= this.latestTs {
		this.latestTs = timestamp
	}
	heap.Push(&this.minHeap, pair2034{price, timestamp})
	heap.Push(&this.maxHeap, pair2034{price, timestamp})
}

func (this *StockPrice) Current() int {
	return this.priceAt[this.latestTs]
}

func (this *StockPrice) Maximum() int {
	for {
		top := this.maxHeap[0]
		if this.priceAt[top.ts] == top.price {
			return top.price
		}
		heap.Pop(&this.maxHeap)
	}
}

func (this *StockPrice) Minimum() int {
	for {
		top := this.minHeap[0]
		if this.priceAt[top.ts] == top.price {
			return top.price
		}
		heap.Pop(&this.minHeap)
	}
}
