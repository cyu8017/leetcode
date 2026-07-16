// LeetCode 0380 - Insert Delete GetRandom O(1)
// https://leetcode.com/problems/insert-delete-getrandom-o1/

import "math/rand"

type RandomizedSet struct {
	values        []int
	indexByValue  map[int]int
}

func Constructor() RandomizedSet {
	return RandomizedSet{
		values:       make([]int, 0),
		indexByValue: make(map[int]int),
	}
}

func (this *RandomizedSet) Insert(val int) bool {
	if _, ok := this.indexByValue[val]; ok {
		return false
	}
	this.indexByValue[val] = len(this.values)
	this.values = append(this.values, val)
	return true
}

func (this *RandomizedSet) Remove(val int) bool {
	index, ok := this.indexByValue[val]
	if !ok {
		return false
	}

	lastValue := this.values[len(this.values)-1]
	this.values[index] = lastValue
	this.indexByValue[lastValue] = index
	this.values = this.values[:len(this.values)-1]
	delete(this.indexByValue, val)
	return true
}

func (this *RandomizedSet) GetRandom() int {
	return this.values[rand.Intn(len(this.values))]
}
