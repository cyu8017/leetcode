// LeetCode 2157 - Groups of Strings
// https://leetcode.com/problems/groups-of-strings/

func groupStrings(words []string) []int {
	parent := map[int]int{}
	size := map[int]int{}
	var find func(int) int
	find = func(x int) int {
		if parent[x] != x {
			parent[x] = find(parent[x])
		}
		return parent[x]
	}
	union := func(a, b int) {
		ra, rb := find(a), find(b)
		if ra == rb {
			return
		}
		if size[ra] < size[rb] {
			ra, rb = rb, ra
		}
		parent[rb] = ra
		size[ra] += size[rb]
	}
	maskOf := func(w string) int {
		m := 0
		for i := 0; i < len(w); i++ {
			m |= 1 << (w[i] - 'a')
		}
		return m
	}
	freq := map[int]int{}
	for _, w := range words {
		m := maskOf(w)
		freq[m]++
	}
	for m, c := range freq {
		parent[m] = m
		size[m] = c
	}
	for m := range freq {
		// delete
		for b := 0; b < 26; b++ {
			if m&(1<<b) != 0 {
				nm := m ^ (1 << b)
				if _, ok := freq[nm]; ok {
					union(m, nm)
				}
				// replace
				for a := 0; a < 26; a++ {
					if nm&(1<<a) == 0 {
						rm := nm | (1 << a)
						if _, ok := freq[rm]; ok {
							union(m, rm)
						}
					}
				}
			} else {
				// add
				nm := m | (1 << b)
				if _, ok := freq[nm]; ok {
					union(m, nm)
				}
			}
		}
	}
	groups, maxSize := 0, 0
	seen := map[int]bool{}
	for m := range freq {
		r := find(m)
		if !seen[r] {
			seen[r] = true
			groups++
			if size[r] > maxSize {
				maxSize = size[r]
			}
		}
	}
	return []int{groups, maxSize}
}
