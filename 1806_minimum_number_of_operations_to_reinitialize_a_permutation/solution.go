// LeetCode 1806 - Minimum Number of Operations to Reinitialize a Permutation
// https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/

func reinitializePermutation(n int) int {
	perm := make([]int, n)
	for i := range perm {
		perm[i] = i
	}
	target := append([]int(nil), perm...)
	operations := 0

	for {
		newPerm := make([]int, n)
		for i := 0; i < n; i++ {
			if i%2 == 0 {
				newPerm[i] = perm[i/2]
			} else {
				newPerm[i] = perm[n/2+(i-1)/2]
			}
		}
		perm = newPerm
		operations++

		equal := true
		for i := range perm {
			if perm[i] != target[i] {
				equal = false
				break
			}
		}
		if equal {
			return operations
		}
	}
}
