// LeetCode 0362 - Design Hit Counter
// https://leetcode.com/problems/design-hit-counter/

type HitCounter struct {
	hits []int
}

func Constructor() HitCounter {
	return HitCounter{hits: make([]int, 0)}
}

func (this *HitCounter) Hit(timestamp int) {
	this.hits = append(this.hits, timestamp)
}

func (this *HitCounter) GetHits(timestamp int) int {
	for len(this.hits) > 0 && this.hits[0] <= timestamp-300 {
		this.hits = this.hits[1:]
	}
	return len(this.hits)
}
