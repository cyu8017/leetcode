// LeetCode 3886 - Sum of Sortable Integers
// https://leetcode.com/problems/sum-of-sortable-integers/

import "sort"

func sumOfSortableIntegers(nums []int) int {
	n := len(nums)
	sorted := append([]int(nil), nums...)
	sort.Ints(sorted)
	divisors := make([]int, 0)
	for d := 1; d*d <= n; d++ {
		if n%d == 0 {
			divisors = append(divisors, d)
			if d*d != n {
				divisors = append(divisors, n/d)
			}
		}
	}
	rotationMatches := func(block, target []int) bool {
		k := len(block)
		prefix := make([]int, k)
		for i := 1; i < k; i++ {
			j := prefix[i-1]
			for j > 0 && target[i] != target[j] {
				j = prefix[j-1]
			}
			if target[i] == target[j] {
				j++
			}
			prefix[i] = j
		}
		matched := 0
		for i := 0; i < 2*k-1; i++ {
			x := block[i%k]
			for matched > 0 && x != target[matched] {
				matched = prefix[matched-1]
			}
			if x == target[matched] {
				matched++
			}
			if matched == k {
				return true
			}
		}
		return false
	}
	answer := 0
	for _, k := range divisors {
		ok := true
		for start := 0; start < n; start += k {
			if !rotationMatches(nums[start:start+k], sorted[start:start+k]) {
				ok = false
				break
			}
		}
		if ok {
			answer += k
		}
	}
	return answer
}