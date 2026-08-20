// LeetCode 2179 - Count Good Triplets in an Array
// https://leetcode.com/problems/count-good-triplets-in-an-array/

type fenwick2179 struct{ bit []int }

func (f *fenwick2179) add(i, v int) {
	for i < len(f.bit) {
		f.bit[i] += v
		i += i & -i
	}
}
func (f *fenwick2179) sum(i int) int {
	s := 0
	for i > 0 {
		s += f.bit[i]
		i -= i & -i
	}
	return s
}

func goodTriplets(nums1 []int, nums2 []int) int64 {
	n := len(nums1)
	pos2 := make([]int, n)
	for i, v := range nums2 {
		pos2[v] = i
	}
	mapped := make([]int, n)
	for i, v := range nums1 {
		mapped[i] = pos2[v]
	}
	left := make([]int, n)
	fw := &fenwick2179{bit: make([]int, n+2)}
	for i := 0; i < n; i++ {
		left[i] = fw.sum(mapped[i])
		fw.add(mapped[i]+1, 1)
	}
	right := make([]int, n)
	fw = &fenwick2179{bit: make([]int, n+2)}
	for i := n - 1; i >= 0; i-- {
		right[i] = fw.sum(n) - fw.sum(mapped[i]+1)
		fw.add(mapped[i]+1, 1)
	}
	var ans int64
	for i := 0; i < n; i++ {
		ans += int64(left[i]) * int64(right[i])
	}
	return ans
}
