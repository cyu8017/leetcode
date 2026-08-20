// LeetCode 2166 - Design Bitset
// https://leetcode.com/problems/design-bitset/

type Bitset struct {
	bits   []byte
	ones   int
	flipped bool
	size   int
}

func Constructor(size int) Bitset {
	return Bitset{bits: make([]byte, size), size: size}
}

func (this *Bitset) Fix(idx int) {
	target := byte(1)
	if this.flipped {
		target = 0
	}
	if this.bits[idx] != target {
		this.bits[idx] = target
		if this.flipped {
			this.ones--
		} else {
			this.ones++
		}
	}
}

func (this *Bitset) Unfix(idx int) {
	target := byte(0)
	if this.flipped {
		target = 1
	}
	if this.bits[idx] != target {
		this.bits[idx] = target
		if this.flipped {
			this.ones++
		} else {
			this.ones--
		}
	}
}

func (this *Bitset) Flip() {
	this.flipped = !this.flipped
	this.ones = this.size - this.ones
}

func (this *Bitset) All() bool {
	return this.ones == this.size
}

func (this *Bitset) One() bool {
	return this.ones > 0
}

func (this *Bitset) Count() int {
	return this.ones
}

func (this *Bitset) ToString() string {
	b := make([]byte, this.size)
	for i := 0; i < this.size; i++ {
		v := this.bits[i]
		if this.flipped {
			v ^= 1
		}
		b[i] = '0' + v
	}
	return string(b)
}
