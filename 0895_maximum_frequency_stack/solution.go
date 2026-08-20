// LeetCode 0895 - Maximum Frequency Stack
// https://leetcode.com/problems/maximum-frequency-stack/

type FreqStack struct {
	freq    map[int]int
	group   map[int][]int
	maxfreq int
}

func Constructor() FreqStack {
	return FreqStack{
		freq:  map[int]int{},
		group: map[int][]int{},
	}
}

func (this *FreqStack) Push(val int) {
	f := this.freq[val] + 1
	this.freq[val] = f
	if f > this.maxfreq {
		this.maxfreq = f
	}
	this.group[f] = append(this.group[f], val)
}

func (this *FreqStack) Pop() int {
	stack := this.group[this.maxfreq]
	val := stack[len(stack)-1]
	this.group[this.maxfreq] = stack[:len(stack)-1]
	this.freq[val]--
	if len(this.group[this.maxfreq]) == 0 {
		this.maxfreq--
	}
	return val
}
