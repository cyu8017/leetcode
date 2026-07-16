// LeetCode 0381 - Insert Delete GetRandom O(1) - Duplicates allowed
// https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

type RandomizedCollection struct {
	values  []int
	indices map[int]map[int]struct{}
}

func Constructor() RandomizedCollection {
	return RandomizedCollection{
		values:  make([]int, 0),
		indices: make(map[int]map[int]struct{}),
	}
}

func (this *RandomizedCollection) Insert(val int) bool {
	if _, ok := this.indices[val]; !ok {
		this.indices[val] = make(map[int]struct{})
	}
	this.indices[val][len(this.values)] = struct{}{}
	this.values = append(this.values, val)
	return len(this.indices[val]) == 1
}

func (this *RandomizedCollection) Remove(val int) bool {
	indexSet, ok := this.indices[val]
	if !ok || len(indexSet) == 0 {
		return false
	}

	var index int
	for position := range indexSet {
		index = position
		break
	}

	lastIndex := len(this.values) - 1
	lastValue := this.values[lastIndex]
	this.values[index] = lastValue
	delete(this.indices[lastValue], lastIndex)
	this.indices[lastValue][index] = struct{}{}
	this.values = this.values[:lastIndex]
	delete(indexSet, index)
	if len(indexSet) == 0 {
		delete(this.indices, val)
	}
	return true
}

func (this *RandomizedCollection) GetRandom() int {
	return this.values[len(this.values)-1]
}
