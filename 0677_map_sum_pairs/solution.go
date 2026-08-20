// LeetCode 0677 - Map Sum Pairs
// https://leetcode.com/problems/map-sum-pairs/

type MapSum struct {
	values     map[string]int
	prefixSums map[string]int
}

func Constructor() MapSum {
	return MapSum{values: map[string]int{}, prefixSums: map[string]int{}}
}

func (m *MapSum) Insert(key string, val int) {
	delta := val - m.values[key]
	m.values[key] = val
	for i := 1; i <= len(key); i++ {
		prefix := key[:i]
		m.prefixSums[prefix] += delta
	}
}

func (m *MapSum) Sum(prefix string) int {
	return m.prefixSums[prefix]
}
