// LeetCode 1966 - Binary Searchable Numbers in an Unsorted Array
// https://leetcode.com/problems/binary-searchable-numbers-in-an-unsorted-array/

func binarySearchableNumbers(nums []int) int {
	n := len(nums)
	ok := make([]int, n)
	for i := range ok {
		ok[i] = 1
	}
	mx := nums[0]
	for i := 1; i < n; i++ {
		if nums[i] < mx {
			ok[i] = 0
		} else {
			mx = nums[i]
		}
	}
	mi := nums[n-1]
	for i := n - 2; i >= 0; i-- {
		if nums[i] > mi {
			ok[i] = 0
		} else {
			mi = nums[i]
		}
	}
	sum := 0
	for _, v := range ok {
		sum += v
	}
	return sum
}
