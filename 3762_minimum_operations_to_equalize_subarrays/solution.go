// LeetCode 3762 - Minimum Operations to Equalize Subarrays
// https://leetcode.com/problems/minimum-operations-to-equalize-subarrays/

import "sort"

type persistentNode3762 struct {
	left, right int
	count       int
	sum         int64
}

func minOperations(nums []int, k int, queries [][]int) []int64 {
	n := len(nums)
	quotient, remainder := make([]int, n), make([]int, n)
	values := make([]int, n)
	for i, x := range nums {
		quotient[i], remainder[i] = x/k, x%k
		values[i] = quotient[i]
	}
	sort.Ints(values)
	unique := values[:0]
	for _, x := range values {
		if len(unique) == 0 || unique[len(unique)-1] != x {
			unique = append(unique, x)
		}
	}
	nodes := []persistentNode3762{{}}
	var update func(int, int, int, int, int) int
	update = func(previous, lo, hi, position, value int) int {
		current := len(nodes)
		nodes = append(nodes, nodes[previous])
		nodes[current].count++
		nodes[current].sum += int64(value)
		if lo < hi {
			mid := (lo + hi) / 2
			if position <= mid {
				nodes[current].left = update(nodes[previous].left, lo, mid, position, value)
			} else {
				nodes[current].right = update(nodes[previous].right, mid+1, hi, position, value)
			}
		}
		return current
	}
	roots := make([]int, n+1)
	for i, x := range quotient {
		position := sort.SearchInts(unique, x)
		roots[i+1] = update(roots[i], 0, len(unique)-1, position, x)
	}
	var kth func(int, int, int, int, int) int
	kth = func(rightRoot, leftRoot, lo, hi, rank int) int {
		if lo == hi {
			return lo
		}
		leftCount := nodes[nodes[rightRoot].left].count - nodes[nodes[leftRoot].left].count
		mid := (lo + hi) / 2
		if rank <= leftCount {
			return kth(nodes[rightRoot].left, nodes[leftRoot].left, lo, mid, rank)
		}
		return kth(nodes[rightRoot].right, nodes[leftRoot].right, mid+1, hi, rank-leftCount)
	}
	var prefixStats func(int, int, int, int, int) (int, int64)
	prefixStats = func(rightRoot, leftRoot, lo, hi, end int) (int, int64) {
		if end < lo {
			return 0, 0
		}
		if hi <= end {
			return nodes[rightRoot].count - nodes[leftRoot].count,
				nodes[rightRoot].sum - nodes[leftRoot].sum
		}
		mid := (lo + hi) / 2
		count, sum := prefixStats(nodes[rightRoot].left, nodes[leftRoot].left, lo, mid, end)
		if end > mid {
			c2, s2 := prefixStats(nodes[rightRoot].right, nodes[leftRoot].right, mid+1, hi, end)
			count, sum = count+c2, sum+s2
		}
		return count, sum
	}
	log := make([]int, n+1)
	for i := 2; i <= n; i++ {
		log[i] = log[i/2] + 1
	}
	levels := log[n] + 1
	minTable, maxTable := make([][]int, levels), make([][]int, levels)
	minTable[0], maxTable[0] = append([]int(nil), remainder...), append([]int(nil), remainder...)
	for level := 1; level < levels; level++ {
		length := n - (1 << level) + 1
		minTable[level], maxTable[level] = make([]int, length), make([]int, length)
		half := 1 << (level - 1)
		for i := 0; i < length; i++ {
			minTable[level][i] = min3762(minTable[level-1][i], minTable[level-1][i+half])
			maxTable[level][i] = max3762(maxTable[level-1][i], maxTable[level-1][i+half])
		}
	}
	answer := make([]int64, len(queries))
	for qi, query := range queries {
		left, right := query[0], query[1]
		length := right - left + 1
		level := log[length]
		offset := right - (1 << level) + 1
		minR := min3762(minTable[level][left], minTable[level][offset])
		maxR := max3762(maxTable[level][left], maxTable[level][offset])
		if minR != maxR {
			answer[qi] = -1
			continue
		}
		medianIndex := kth(roots[right+1], roots[left], 0, len(unique)-1, (length+1)/2)
		median := unique[medianIndex]
		leftCount, leftSum := prefixStats(roots[right+1], roots[left], 0, len(unique)-1, medianIndex)
		totalSum := nodes[roots[right+1]].sum - nodes[roots[left]].sum
		answer[qi] = int64(median*leftCount) - leftSum +
			(totalSum-leftSum)-int64(median*(length-leftCount))
	}
	return answer
}

func min3762(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max3762(a, b int) int {
	if a > b {
		return a
	}
	return b
}