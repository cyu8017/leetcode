// LeetCode 2526 - Find Consecutive Integers from a Data Stream
// https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

type DataStream struct {
	value, k, streak int
}

func Constructor(value int, k int) DataStream {
	return DataStream{value: value, k: k}
}

func (d *DataStream) Consec(num int) bool {
	if num == d.value {
		d.streak++
	} else {
		d.streak = 0
	}
	return d.streak >= d.k
}
