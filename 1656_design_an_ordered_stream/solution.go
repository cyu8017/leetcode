// LeetCode 1656 - Design an Ordered Stream
// https://leetcode.com/problems/design-an-ordered-stream/

type OrderedStream struct {
	a []string
	p int
}

func Constructor(n int) OrderedStream {
	return OrderedStream{a: make([]string, n+1), p: 1}
}

func (this *OrderedStream) Insert(idKey int, value string) []string {
	this.a[idKey] = value
	out := []string{}
	for this.p < len(this.a) && this.a[this.p] != "" {
		out = append(out, this.a[this.p])
		this.p++
	}
	return out
}
