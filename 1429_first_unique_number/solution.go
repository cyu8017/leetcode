// LeetCode 1429 - First Unique Number
// https://leetcode.com/problems/first-unique-number/

type FirstUnique struct {
	counts map[int]int
	order  []int
	pos    map[int]int
}

func Constructor(nums []int) FirstUnique {
	f := FirstUnique{counts: map[int]int{}, pos: map[int]int{}}
	for _, v := range nums {
		f.Add(v)
	}
	return f
}

func (this *FirstUnique) ShowFirstUnique() int {
	for _, v := range this.order {
		if this.counts[v] == 1 {
			return v
		}
	}
	return -1
}

func (this *FirstUnique) Add(value int) {
	this.counts[value]++
	if this.counts[value] == 1 {
		this.order = append(this.order, value)
	}
}
