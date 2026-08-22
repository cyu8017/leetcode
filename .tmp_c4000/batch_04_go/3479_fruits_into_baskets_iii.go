// LeetCode 3479 - Fruits Into Baskets III
// https://leetcode.com/problems/fruits-into-baskets-iii/

func numOfUnplacedFruits(fruits []int, baskets []int) int {
	n := len(baskets)
	size := 1
	for size < n {
		size <<= 1
	}
	tree := make([]int, size*2)
	for i := 0; i < n; i++ {
		tree[size+i] = baskets[i]
	}
	for i := size - 1; i > 0; i-- {
		tree[i] = tree[i*2]
		if tree[i*2+1] > tree[i] {
			tree[i] = tree[i*2+1]
		}
	}
	var find func(int, int, int, int) int
	find = func(node, nl, nr, need int) int {
		if tree[node] < need {
			return -1
		}
		if nl == nr {
			return nl
		}
		mid := (nl + nr) / 2
		left := find(node*2, nl, mid, need)
		if left != -1 {
			return left
		}
		return find(node*2+1, mid+1, nr, need)
	}
	update := func(idx int) {
		p := size + idx
		tree[p] = -1
		for p >>= 1; p > 0; p >>= 1 {
			tree[p] = tree[p*2]
			if tree[p*2+1] > tree[p] {
				tree[p] = tree[p*2+1]
			}
		}
	}
	unplaced := 0
	for _, f := range fruits {
		idx := find(1, 0, size-1, f)
		if idx == -1 || idx >= n {
			unplaced++
		} else {
			update(idx)
		}
	}
	return unplaced
}
