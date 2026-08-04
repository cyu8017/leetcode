// LeetCode 1286 - Iterator for Combination
// https://leetcode.com/problems/iterator-for-combination/

type CombinationIterator struct {
	items []string
	idx   int
}

func Constructor(characters string, combinationLength int) CombinationIterator {
	items := []string{}
	var dfs func(int, []byte)
	dfs = func(start int, cur []byte) {
		if len(cur) == combinationLength {
			items = append(items, string(cur))
			return
		}
		for i := start; i < len(characters); i++ {
			dfs(i+1, append(cur, characters[i]))
		}
	}
	dfs(0, nil)
	return CombinationIterator{items: items}
}

func (this *CombinationIterator) Next() string {
	v := this.items[this.idx]
	this.idx++
	return v
}

func (this *CombinationIterator) HasNext() bool {
	return this.idx < len(this.items)
}
