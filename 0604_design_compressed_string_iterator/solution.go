// LeetCode 0604 - Design Compressed String Iterator
// https://leetcode.com/problems/design-compressed-string-iterator/

type StringIterator struct {
	chars  []byte
	counts []int
	index  int
}

func Constructor(compressedString string) StringIterator {
	chars := []byte{}
	counts := []int{}
	i, n := 0, len(compressedString)
	for i < n {
		ch := compressedString[i]
		i++
		j := i
		for j < n && compressedString[j] >= '0' && compressedString[j] <= '9' {
			j++
		}
		count := 0
		for _, d := range compressedString[i:j] {
			count = count*10 + int(d-'0')
		}
		chars = append(chars, ch)
		counts = append(counts, count)
		i = j
	}
	return StringIterator{chars: chars, counts: counts}
}

func (it *StringIterator) Next() byte {
	if !it.HasNext() {
		return ' '
	}
	ch := it.chars[it.index]
	it.counts[it.index]--
	if it.counts[it.index] == 0 {
		it.index++
	}
	return ch
}

func (it *StringIterator) HasNext() bool {
	return it.index < len(it.chars)
}
