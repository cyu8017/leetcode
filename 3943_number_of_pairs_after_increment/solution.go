// LeetCode 3943 - Number of Pairs After Increment
// https://leetcode.com/problems/number-of-pairs-after-increment/

func numberOfPairs(nums1 []int, nums2 []int, queries [][]int) []int64 {
	const blockSize = 225
	n := len(nums2)
	blocks := (n + blockSize - 1) / blockSize
	lazy := make([]int, blocks)
	freq := make([]map[int]int, blocks)
	rebuild := func(b int) {
		freq[b] = make(map[int]int)
		end := (b + 1) * blockSize
		if end > n {
			end = n
		}
		for i := b * blockSize; i < end; i++ {
			freq[b][nums2[i]]++
		}
	}
	push := func(b int) {
		if lazy[b] != 0 {
			end := (b + 1) * blockSize
			if end > n {
				end = n
			}
			for i := b * blockSize; i < end; i++ {
				nums2[i] += lazy[b]
			}
			lazy[b] = 0
		}
	}
	for b := 0; b < blocks; b++ {
		rebuild(b)
	}
	fixed := make(map[int]int)
	for _, x := range nums1 {
		fixed[x]++
	}
	answer := make([]int64, 0)
	for _, q := range queries {
		if q[0] == 1 {
			l, r, delta := q[1], q[2], q[3]
			first, last := l/blockSize, r/blockSize
			if first == last {
				push(first)
				for i := l; i <= r; i++ {
					nums2[i] += delta
				}
				rebuild(first)
				continue
			}
			push(first)
			for i := l; i < (first+1)*blockSize; i++ {
				nums2[i] += delta
			}
			rebuild(first)
			push(last)
			for i := last * blockSize; i <= r; i++ {
				nums2[i] += delta
			}
			rebuild(last)
			for b := first + 1; b < last; b++ {
				lazy[b] += delta
			}
		} else {
			var total int64
			for a, countA := range fixed {
				target := q[1] - a
				for b := 0; b < blocks; b++ {
					total += int64(countA * freq[b][target-lazy[b]])
				}
			}
			answer = append(answer, total)
		}
	}
	return answer
}