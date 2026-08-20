// LeetCode 2213 - Longest Substring of One Repeating Character
// https://leetcode.com/problems/longest-substring-of-one-repeating-character/

type seg2213 struct {
	lChar, rChar byte
	lLen, rLen, best, size int
}

type SegTree2213 struct {
	n    int
	tree []seg2213
	s    []byte
}

func merge2213(a, b seg2213) seg2213 {
	if a.size == 0 {
		return b
	}
	if b.size == 0 {
		return a
	}
	res := seg2213{lChar: a.lChar, rChar: b.rChar, size: a.size + b.size, best: a.best}
	if b.best > res.best {
		res.best = b.best
	}
	res.lLen = a.lLen
	res.rLen = b.rLen
	if a.rChar == b.lChar {
		mid := a.rLen + b.lLen
		if mid > res.best {
			res.best = mid
		}
		if a.lLen == a.size {
			res.lLen = a.size + b.lLen
		}
		if b.rLen == b.size {
			res.rLen = b.size + a.rLen
		}
	}
	return res
}

func (st *SegTree2213) build(idx, l, r int) {
	if l == r {
		st.tree[idx] = seg2213{st.s[l], st.s[l], 1, 1, 1, 1}
		return
	}
	mid := (l + r) / 2
	st.build(idx*2, l, mid)
	st.build(idx*2+1, mid+1, r)
	st.tree[idx] = merge2213(st.tree[idx*2], st.tree[idx*2+1])
}

func (st *SegTree2213) update(idx, l, r, pos int, ch byte) {
	if l == r {
		st.s[pos] = ch
		st.tree[idx] = seg2213{ch, ch, 1, 1, 1, 1}
		return
	}
	mid := (l + r) / 2
	if pos <= mid {
		st.update(idx*2, l, mid, pos, ch)
	} else {
		st.update(idx*2+1, mid+1, r, pos, ch)
	}
	st.tree[idx] = merge2213(st.tree[idx*2], st.tree[idx*2+1])
}

func longestRepeating(s string, queryCharacters string, queryIndices []int) []int {
	st := &SegTree2213{n: len(s), tree: make([]seg2213, 4*len(s)+5), s: []byte(s)}
	st.build(1, 0, st.n-1)
	ans := make([]int, len(queryIndices))
	for i := range queryIndices {
		st.update(1, 0, st.n-1, queryIndices[i], queryCharacters[i])
		ans[i] = st.tree[1].best
	}
	return ans
}
