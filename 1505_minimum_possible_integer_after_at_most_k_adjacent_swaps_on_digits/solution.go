// LeetCode 1505 - Minimum Possible Integer After at Most K Adjacent Swaps On Digits
// https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/

type fenwick struct{ bit []int }

func newFenwick(n int) *fenwick {
	return &fenwick{bit: make([]int, n+1)}
}

func (f *fenwick) add(i, delta int) {
	i++
	for i < len(f.bit) {
		f.bit[i] += delta
		i += i & -i
	}
}

func (f *fenwick) sum(i int) int {
	out := 0
	for i > 0 {
		out += f.bit[i]
		i -= i & -i
	}
	return out
}

func minInteger(num string, k int) string {
	positions := make([][]int, 10)
	for i, ch := range num {
		d := int(ch - '0')
		positions[d] = append(positions[d], i)
	}
	heads := make([]int, 10)
	fw := newFenwick(len(num))
	out := make([]byte, 0, len(num))
	for range num {
		for digit := 0; digit < 10; digit++ {
			if heads[digit] >= len(positions[digit]) {
				continue
			}
			index := positions[digit][heads[digit]]
			cost := index - fw.sum(index)
			if cost <= k {
				k -= cost
				heads[digit]++
				fw.add(index, 1)
				out = append(out, byte('0'+digit))
				break
			}
		}
	}
	return string(out)
}
