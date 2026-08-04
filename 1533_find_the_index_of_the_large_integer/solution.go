// LeetCode 1533 - Find the Index of the Large Integer
// https://leetcode.com/problems/find-the-index-of-the-large-integer/

type ArrayReader struct {
	arr []int
}

func (this *ArrayReader) compareSub(l, r, x, y int) int {
	a, b := 0, 0
	for i := l; i <= r; i++ {
		a += this.arr[i]
	}
	for i := x; i <= y; i++ {
		b += this.arr[i]
	}
	if a > b {
		return 1
	}
	if a < b {
		return -1
	}
	return 0
}

func (this *ArrayReader) length() int {
	return len(this.arr)
}

func getIndex(arr []int) int {
	reader := &ArrayReader{arr: arr}
	left, right := 0, reader.length()-1
	for left < right {
		length := right - left + 1
		half := length / 2
		result := reader.compareSub(left, left+half-1, right-half+1, right)
		if result == 0 {
			return left + half
		}
		if result > 0 {
			right = left + half - 1
		} else {
			left = right - half + 1
		}
	}
	return left
}
