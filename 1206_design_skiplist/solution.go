// LeetCode 1206 - Design Skiplist
// https://leetcode.com/problems/design-skiplist/

import "sort"

type Skiplist struct {
	values []int
}

func Constructor() Skiplist {
	return Skiplist{values: []int{}}
}

func (this *Skiplist) Search(target int) bool {
	i := sort.SearchInts(this.values, target)
	return i < len(this.values) && this.values[i] == target
}

func (this *Skiplist) Add(num int) {
	i := sort.SearchInts(this.values, num)
	this.values = append(this.values, 0)
	copy(this.values[i+1:], this.values[i:])
	this.values[i] = num
}

func (this *Skiplist) Erase(num int) bool {
	i := sort.SearchInts(this.values, num)
	if i == len(this.values) || this.values[i] != num {
		return false
	}
	this.values = append(this.values[:i], this.values[i+1:]...)
	return true
}
