// LeetCode 0705 - Design HashSet
// https://leetcode.com/problems/design-hashset/

type MyHashSet struct {
	data map[int]struct{}
}

func Constructor() MyHashSet {
	return MyHashSet{data: map[int]struct{}{}}
}

func (this *MyHashSet) Add(key int) {
	this.data[key] = struct{}{}
}

func (this *MyHashSet) Remove(key int) {
	delete(this.data, key)
}

func (this *MyHashSet) Contains(key int) bool {
	_, ok := this.data[key]
	return ok
}
