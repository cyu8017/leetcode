// LeetCode 1664 - Ways to Make a Fair Array
// https://leetcode.com/problems/ways-to-make-a-fair-array/

func waysToMakeFair(nums []int) int {
	te, to := 0, 0
	for i, x := range nums {
		if i%2 == 0 {
			te += x
		} else {
			to += x
		}
	}
	le, lo, ans := 0, 0, 0
	for i, x := range nums {
		if i%2 == 1 {
			to -= x
		} else {
			te -= x
		}
		if le+to == lo+te {
			ans++
		}
		if i%2 == 1 {
			lo += x
		} else {
			le += x
		}
	}
	return ans
}
