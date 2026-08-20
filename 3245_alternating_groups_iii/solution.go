// LeetCode 3245 - Alternating Groups III
// https://leetcode.com/problems/alternating-groups-iii/

type segmentTree3245 struct {
	n                     int
	treeIntervalCounts    []int
	treeIntervalLengths   []int
}

func newSegmentTree3245(n int) *segmentTree3245 {
	return &segmentTree3245{
		n:                   n,
		treeIntervalCounts:  make([]int, 4*n),
		treeIntervalLengths: make([]int, 4*n),
	}
}

func (st *segmentTree3245) add(i, val int) {
	st.addRec(0, 0, st.n-1, i, val)
}

func (st *segmentTree3245) addRec(treeIndex, lo, hi, i, val int) {
	if lo == hi {
		st.treeIntervalCounts[treeIndex] += val
		st.treeIntervalLengths[treeIndex] = st.treeIntervalCounts[treeIndex] * i
		return
	}
	mid := (lo + hi) / 2
	if i <= mid {
		st.addRec(2*treeIndex+1, lo, mid, i, val)
	} else {
		st.addRec(2*treeIndex+2, mid+1, hi, i, val)
	}
	st.treeIntervalCounts[treeIndex] = st.treeIntervalCounts[2*treeIndex+1] + st.treeIntervalCounts[2*treeIndex+2]
	st.treeIntervalLengths[treeIndex] = st.treeIntervalLengths[2*treeIndex+1] + st.treeIntervalLengths[2*treeIndex+2]
}

func (st *segmentTree3245) queryIntervalCounts(i int) int {
	return st.query(st.treeIntervalCounts, 0, 0, st.n-1, i, st.n-1)
}

func (st *segmentTree3245) queryIntervalLengths(i int) int {
	return st.query(st.treeIntervalLengths, 0, 0, st.n-1, i, st.n-1)
}

func (st *segmentTree3245) query(tree []int, treeIndex, lo, hi, i, j int) int {
	if i <= lo && hi <= j {
		return tree[treeIndex]
	}
	if j < lo || hi < i {
		return 0
	}
	mid := (lo + hi) / 2
	return st.query(tree, treeIndex*2+1, lo, mid, i, j) + st.query(tree, treeIndex*2+2, mid+1, hi, i, j)
}

type intervalKey struct{ l, r int }

func numberOfAlternatingGroups(colors []int, queries [][]int) []int {
	n := len(colors)
	ans := []int{}
	arr := append(append([]int{}, colors...), colors[:n-1]...)
	tree := newSegmentTree3245(2*n - 1)
	intervals := map[intervalKey]struct{}{}

	insert := func(l, r int) {
		intervals[intervalKey{l, r}] = struct{}{}
		if l < n {
			tree.add(r-l+1, 1)
		}
	}
	remove := func(l, r int) {
		delete(intervals, intervalKey{l, r})
		if l < n {
			tree.add(r-l+1, -1)
		}
	}
	findInterval := func(target int) (int, int) {
		bestL, bestR := -1, -1
		for k := range intervals {
			if k.l <= target && target <= k.r {
				if k.l > bestL {
					bestL, bestR = k.l, k.r
				}
			}
		}
		return bestL, bestR
	}
	getNum := func(sz int) int {
		numIntervals := tree.queryIntervalCounts(sz)
		sumIntervals := tree.queryIntervalLengths(sz)
		numAlternatingGroups := sumIntervals - numIntervals*sz + numIntervals
		l, r := findInterval(n)
		if l < 0 || l >= n || r-l+1 < sz {
			return numAlternatingGroups
		}
		if r >= n {
			nonDuplicateGroups := n - l
			numGroups := (r - l + 1) - sz + 1
			extra := numGroups - nonDuplicateGroups
			if extra > 0 {
				numAlternatingGroups -= extra
			}
		}
		return numAlternatingGroups
	}
	update := func(index, color int) {
		if arr[index] == color {
			return
		}
		arr[index] = color
		start, end := findInterval(index)
		remove(start, end)
		if start < index && index < end {
			insert(start, index-1)
			insert(index, index)
			insert(index+1, end)
			return
		}
		if start == index && index < end {
			insert(start+1, end)
		}
		if start < index && index == end {
			insert(start, end-1)
		}
		ns, ne := index, index
		// merge left
		for {
			merged := false
			for k := range intervals {
				if k.r+1 == ns && arr[k.r] != arr[ns] {
					remove(k.l, k.r)
					ns = k.l
					merged = true
					break
				}
			}
			if !merged {
				break
			}
		}
		// merge right
		for {
			merged := false
			for k := range intervals {
				if k.l == ne+1 && arr[k.l] != arr[ne] {
					remove(k.l, k.r)
					ne = k.r
					merged = true
					break
				}
			}
			if !merged {
				break
			}
		}
		insert(ns, ne)
	}

	start := 0
	for i := 1; i < 2*n-1; i++ {
		if arr[i] == arr[i-1] {
			insert(start, i-1)
			start = i
		}
	}
	insert(start, 2*n-2)

	for _, query := range queries {
		if query[0] == 1 {
			ans = append(ans, getNum(query[1]))
		} else {
			index, color := query[1], query[2]
			if arr[index] != color {
				update(index, color)
				if index < n-1 {
					update(index+n, color)
				}
			}
		}
	}
	return ans
}
