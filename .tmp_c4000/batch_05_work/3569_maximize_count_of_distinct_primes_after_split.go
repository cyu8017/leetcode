// LeetCode 3569 - Maximize Count of Distinct Primes After Split
// https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/

func maximumCount(nums []int, queries [][]int) []int {
	mx := 0
	for _, v := range nums {
		if v > mx {
			mx = v
		}
	}
	for _, q := range queries {
		if q[1] > mx {
			mx = q[1]
		}
	}
	isP := make([]bool, mx+1)
	for i := 2; i <= mx; i++ {
		isP[i] = true
	}
	for i := 2; i*i <= mx; i++ {
		if isP[i] {
			for j := i * i; j <= mx; j += i {
				isP[j] = false
			}
		}
	}
	ans := make([]int, len(queries))
	for qi, q := range queries {
		nums[q[0]] = q[1]
		best := 0
		left := map[int]int{}
		right := map[int]int{}
		for _, v := range nums {
			if v <= mx && isP[v] {
				right[v]++
			}
		}
		for i := 0; i < len(nums)-1; i++ {
			v := nums[i]
			if v <= mx && isP[v] {
				left[v]++
				right[v]--
				if right[v] == 0 {
					delete(right, v)
				}
			}
			cur := len(left) + len(right)
			if cur > best {
				best = cur
			}
		}
		ans[qi] = best
	}
	return ans
}
