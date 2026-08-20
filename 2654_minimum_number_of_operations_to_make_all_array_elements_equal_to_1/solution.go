// LeetCode 2654 - Minimum Number of Operations to Make All Array Elements Equal to 1
// https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/


func minOperations(nums []int) int {
	n := len(nums)
	ones := 0
	for _, x := range nums {
		if x == 1 {
			ones++
		}
	}
	if ones > 0 {
		return n - ones
	}
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}
	best := n + 1
	for i := 0; i < n; i++ {
		g := 0
		for j := i; j < n; j++ {
			g = gcd(g, nums[j])
			if g == 1 {
				if j-i < best {
					best = j - i
				}
				break
			}
		}
	}
	if best == n+1 {
		return -1
	}
	return best + n - 1
}
