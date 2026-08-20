// LeetCode 2031 - Count Subarrays With More Ones Than Zeros
// https://leetcode.com/problems/count-subarrays-with-more-ones-than-zeros/

type fenwick2031 struct {
	bit []int
}

func newFenwick2031(n int) *fenwick2031 {
	return &fenwick2031{bit: make([]int, n+2)}
}

func (f *fenwick2031) add(i, v int) {
	for i < len(f.bit) {
		f.bit[i] += v
		i += i & -i
	}
}

func (f *fenwick2031) sum(i int) int {
	s := 0
	for i > 0 {
		s += f.bit[i]
		i -= i & -i
	}
	return s
}

func subarraysWithMoreZerosThanOnes(nums []int) int {
	// Actually: more ones than zeros
	const MOD = 1_000_000_007
	n := len(nums)
	// prefix sum of +1 for 1 and -1 for 0, count pairs where pref[r]-pref[l] > 0
	offset := n + 1
	fw := newFenwick2031(2*n + 5)
	pref := 0
	fw.add(offset, 1)
	ans := 0
	for _, x := range nums {
		if x == 1 {
			pref++
		} else {
			pref--
		}
		idx := pref + offset
		ans = (ans + fw.sum(idx-1)) % MOD
		fw.add(idx, 1)
	}
	return ans
}
