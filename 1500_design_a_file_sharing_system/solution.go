// LeetCode 1500 - Design a File Sharing System
// https://leetcode.com/problems/design-a-file-sharing-system/

import "container/heap"
import "sort"

type FileSharing struct {
	owners map[int]map[int]bool
	chunks map[int]map[int]bool
	free   *intHeap
	nextID int
}

type intHeap []int

func (h intHeap) Len() int            { return len(h) }
func (h intHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h intHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *intHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *intHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func Constructor(m int) FileSharing {
	h := &intHeap{}
	heap.Init(h)
	return FileSharing{
		owners: make(map[int]map[int]bool),
		chunks: make(map[int]map[int]bool),
		free:   h,
		nextID: 1,
	}
}

func (this *FileSharing) Join(ownedChunks []int) int {
	user := this.nextID
	if this.free.Len() > 0 {
		user = heap.Pop(this.free).(int)
	} else {
		this.nextID++
	}
	this.chunks[user] = make(map[int]bool)
	for _, chunk := range ownedChunks {
		this.chunks[user][chunk] = true
		if this.owners[chunk] == nil {
			this.owners[chunk] = make(map[int]bool)
		}
		this.owners[chunk][user] = true
	}
	return user
}

func (this *FileSharing) Leave(userID int) {
	for chunk := range this.chunks[userID] {
		delete(this.owners[chunk], userID)
	}
	delete(this.chunks, userID)
	heap.Push(this.free, userID)
}

func (this *FileSharing) Request(userID int, chunkID int) []int {
	users := make([]int, 0, len(this.owners[chunkID]))
	for u := range this.owners[chunkID] {
		users = append(users, u)
	}
	sort.Ints(users)
	if len(users) > 0 {
		if this.chunks[userID] == nil {
			this.chunks[userID] = make(map[int]bool)
		}
		this.chunks[userID][chunkID] = true
		if this.owners[chunkID] == nil {
			this.owners[chunkID] = make(map[int]bool)
		}
		this.owners[chunkID][userID] = true
	}
	return users
}
