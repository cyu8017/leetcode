// LeetCode 1979 - Find Greatest Common Divisor of Array
// https://leetcode.com/problems/find-greatest-common-divisor-of-array/

func findGCD(nums []int) int {
	mn, mx := nums[0], nums[0]
	for _, x := range nums {
		if x < mn {
			mn = x
		}
		if x > mx {
			mx = x
		}
	}
	return gcd1979(mn, mx)
}

func gcd1979(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
