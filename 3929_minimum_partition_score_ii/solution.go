// LeetCode 3929 - Minimum Partition Score II
// https://leetcode.com/problems/minimum-partition-score-ii/

type partitionLine3929 struct {
	slope, intercept int64
	count            int
	valid            bool
}

type partitionState3929 struct {
	value int64
	count int
	valid bool
}

func minPartitionScore(nums []int, k int) int64 {
	n := len(nums)
	prefix := make([]int64, n+1)
	for i, value := range nums {
		prefix[i+1] = prefix[i] + int64(value)
	}
	better := func(a, b partitionState3929) partitionState3929 {
		if !a.valid {
			return b
		}
		if !b.valid {
			return a
		}
		if a.value != b.value {
			if a.value < b.value {
				return a
			}
			return b
		}
		if a.count >= b.count {
			return a
		}
		return b
	}
	evaluate := func(line partitionLine3929, x int64) partitionState3929 {
		if !line.valid {
			return partitionState3929{}
		}
		return partitionState3929{line.slope*x + line.intercept, line.count, true}
	}
	run := func(penalty int64) partitionState3929 {
		tree := make([]partitionLine3929, 4*(n+1))
		var insert func(int, int, int, partitionLine3929)
		insert = func(node, left, right int, line partitionLine3929) {
			if !tree[node].valid {
				tree[node] = line
				return
			}
			mid := (left + right) / 2
			xLeft, xMid := prefix[left], prefix[mid]
			leftBetter := better(evaluate(line, xLeft), evaluate(tree[node], xLeft))
			midBetter := better(evaluate(line, xMid), evaluate(tree[node], xMid))
			lineWinsLeft := leftBetter.value == evaluate(line, xLeft).value &&
				leftBetter.count == line.count
			lineWinsMid := midBetter.value == evaluate(line, xMid).value &&
				midBetter.count == line.count
			if lineWinsMid {
				tree[node], line = line, tree[node]
			}
			if left == right {
				return
			}
			if lineWinsLeft != lineWinsMid {
				insert(node*2, left, mid, line)
			} else {
				insert(node*2+1, mid+1, right, line)
			}
		}
		var query func(int, int, int, int) partitionState3929
		query = func(node, left, right, index int) partitionState3929 {
			result := evaluate(tree[node], prefix[index])
			if left == right {
				return result
			}
			mid := (left + right) / 2
			if index <= mid {
				return better(result, query(node*2, left, mid, index))
			}
			return better(result, query(node*2+1, mid+1, right, index))
		}
		insert(1, 0, n, partitionLine3929{0, 0, 0, true})
		var current partitionState3929
		for i := 1; i <= n; i++ {
			best := query(1, 0, n, i)
			x := prefix[i]
			current = partitionState3929{
				best.value + x*x + x + penalty,
				best.count + 1,
				true,
			}
			insert(1, 0, n, partitionLine3929{
				-2 * x,
				current.value + x*x - x,
				current.count,
				true,
			})
		}
		return current
	}
	bound := prefix[n]*prefix[n] + prefix[n] + 1
	low, high := int64(0), bound
	for low < high {
		mid := low + (high-low+1)/2
		if run(mid).count >= k {
			low = mid
		} else {
			high = mid - 1
		}
	}
	state := run(low)
	return (state.value - low*int64(k)) / 2
}