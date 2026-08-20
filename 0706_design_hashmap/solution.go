// LeetCode 0706 - Design HashMap
// https://leetcode.com/problems/design-hashmap/

type MyHashMap struct {
	data map[int]int
}

func Constructor() MyHashMap {
	return MyHashMap{data: map[int]int{}}
}

func (this *MyHashMap) Put(key int, value int) {
	this.data[key] = value
}

func (this *MyHashMap) Get(key int) int {
	if v, ok := this.data[key]; ok {
		return v
	}
	return -1
}

func (this *MyHashMap) Remove(key int) {
	delete(this.data, key)
}
