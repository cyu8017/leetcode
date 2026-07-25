// LeetCode 1622 - Fancy Sequence
// https://leetcode.com/problems/fancy-sequence/

type Fancy struct {
	vals []int
	mul  int
	add  int
}

const fancyMod = 1000000007

func Constructor() Fancy {
	return Fancy{mul: 1, add: 0}
}

func (this *Fancy) Append(val int) {
	inv := fancyModPow(this.mul, fancyMod-2)
	v := ((val-this.add)%fancyMod+fancyMod)%fancyMod * inv % fancyMod
	this.vals = append(this.vals, v)
}

func (this *Fancy) AddAll(inc int) {
	if len(this.vals) > 0 {
		this.add = (this.add + inc) % fancyMod
	}
}

func (this *Fancy) MultAll(m int) {
	if len(this.vals) == 0 {
		return
	}
	this.mul = this.mul * m % fancyMod
	this.add = this.add * m % fancyMod
}

func (this *Fancy) GetIndex(idx int) int {
	if idx >= len(this.vals) {
		return -1
	}
	return (this.vals[idx]*this.mul + this.add) % fancyMod
}

func fancyModPow(base, exp int) int {
	res := 1
	base %= fancyMod
	for exp > 0 {
		if exp&1 == 1 {
			res = res * base % fancyMod
		}
		base = base * base % fancyMod
		exp >>= 1
	}
	return res
}
