// LeetCode 2584 - Split the Array to Make Coprime Products
// https://leetcode.com/problems/split-the-array-to-make-coprime-products/


func findValidSplit(nums []int) int {
	n := len(nums)
	first := map[int]int{}
	last := map[int]int{}
	factorize := func(x, idx int) {
		for p := 2; p*p <= x; p++ {
			if x%p == 0 {
				if _, ok := first[p]; !ok {
					first[p] = idx
				}
				last[p] = idx
				for x%p == 0 {
					x /= p
				}
			}
		}
		if x > 1 {
			if _, ok := first[x]; !ok {
				first[x] = idx
			}
			last[x] = idx
		}
	}
	for i, x := range nums {
		factorize(x, i)
	}
	far := 0
	for i := 0; i < n-1; i++ {
		x := nums[i]
		for p := 2; p*p <= x; p++ {
			if x%p == 0 {
				if last[p] > far {
					far = last[p]
				}
				for x%p == 0 {
					x /= p
				}
			}
		}
		if x > 1 && last[x] > far {
			far = last[x]
		}
		if far == i {
			return i
		}
	}
	return -1
}
