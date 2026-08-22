// LeetCode 3815 - Design Auction System
// https://leetcode.com/problems/design-auction-system/

import "container/heap"

type auctionBid struct {
	amount int
	userID int
}

type auctionHeap []auctionBid

func (h auctionHeap) Len() int { return len(h) }
func (h auctionHeap) Less(i, j int) bool {
	if h[i].amount != h[j].amount {
		return h[i].amount > h[j].amount
	}
	return h[i].userID > h[j].userID
}
func (h auctionHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *auctionHeap) Push(value any) {
	*h = append(*h, value.(auctionBid))
}
func (h *auctionHeap) Pop() any {
	old := *h
	value := old[len(old)-1]
	*h = old[:len(old)-1]
	return value
}

type AuctionSystem struct {
	bids  map[int]map[int]int
	heaps map[int]*auctionHeap
}

func Constructor() AuctionSystem {
	return AuctionSystem{
		bids:  make(map[int]map[int]int),
		heaps: make(map[int]*auctionHeap),
	}
}

func (system *AuctionSystem) AddBid(userId int, itemId int, bidAmount int) {
	if system.bids[itemId] == nil {
		system.bids[itemId] = make(map[int]int)
	}
	if system.heaps[itemId] == nil {
		h := &auctionHeap{}
		heap.Init(h)
		system.heaps[itemId] = h
	}
	system.bids[itemId][userId] = bidAmount
	heap.Push(system.heaps[itemId], auctionBid{bidAmount, userId})
}

func (system *AuctionSystem) UpdateBid(userId int, itemId int, newAmount int) {
	system.AddBid(userId, itemId, newAmount)
}

func (system *AuctionSystem) RemoveBid(userId int, itemId int) {
	delete(system.bids[itemId], userId)
}

func (system *AuctionSystem) GetHighestBidder(itemId int) int {
	h := system.heaps[itemId]
	for h != nil && h.Len() > 0 {
		top := (*h)[0]
		if amount, exists := system.bids[itemId][top.userID]; exists && amount == top.amount {
			return top.userID
		}
		heap.Pop(h)
	}
	return -1
}