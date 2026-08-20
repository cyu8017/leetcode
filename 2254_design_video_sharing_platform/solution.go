// LeetCode 2254 - Design Video Sharing Platform
// https://leetcode.com/problems/design-video-sharing-platform/

import "container/heap"

type IntHeap []int

func (h IntHeap) Len() int            { return len(h) }
func (h IntHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type VideoSharingPlatform struct {
	nextID int
	free   IntHeap
	videos map[int]string
	views  map[int]int
	likes  map[int]int
	dislikes map[int]int
}

func Constructor() VideoSharingPlatform {
	h := IntHeap{}
	heap.Init(&h)
	return VideoSharingPlatform{
		videos:   map[int]string{},
		views:    map[int]int{},
		likes:    map[int]int{},
		dislikes: map[int]int{},
		free:     h,
	}
}

func (this *VideoSharingPlatform) Upload(video string) int {
	var id int
	if this.free.Len() > 0 {
		id = heap.Pop(&this.free).(int)
	} else {
		id = this.nextID
		this.nextID++
	}
	this.videos[id] = video
	this.views[id] = 0
	this.likes[id] = 0
	this.dislikes[id] = 0
	return id
}

func (this *VideoSharingPlatform) Remove(videoId int) {
	if _, ok := this.videos[videoId]; !ok {
		return
	}
	delete(this.videos, videoId)
	delete(this.views, videoId)
	delete(this.likes, videoId)
	delete(this.dislikes, videoId)
	heap.Push(&this.free, videoId)
}

func (this *VideoSharingPlatform) Watch(videoId int, startMinute int, endMinute int) string {
	v, ok := this.videos[videoId]
	if !ok {
		return "-1"
	}
	this.views[videoId]++
	if startMinute >= len(v) {
		return ""
	}
	if endMinute >= len(v) {
		endMinute = len(v) - 1
	}
	return v[startMinute : endMinute+1]
}

func (this *VideoSharingPlatform) Like(videoId int) {
	if _, ok := this.videos[videoId]; ok {
		this.likes[videoId]++
	}
}

func (this *VideoSharingPlatform) Dislike(videoId int) {
	if _, ok := this.videos[videoId]; ok {
		this.dislikes[videoId]++
	}
}

func (this *VideoSharingPlatform) GetLikesAndDislikes(videoId int) []int {
	if _, ok := this.videos[videoId]; !ok {
		return []int{-1}
	}
	return []int{this.likes[videoId], this.dislikes[videoId]}
}

func (this *VideoSharingPlatform) GetViews(videoId int) int {
	if _, ok := this.videos[videoId]; !ok {
		return -1
	}
	return this.views[videoId]
}
