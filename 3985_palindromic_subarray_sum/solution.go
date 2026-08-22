// LeetCode 3985 - Palindromic Subarray Sum
// https://leetcode.com/problems/palindromic-subarray-sum/

func maxPalindromicSubarraySum(nums []int) int64 {
	n := len(nums)
	prefix := make([]int64, n+1)
	for i, x := range nums {
		prefix[i+1] = prefix[i] + int64(x)
	}
	odd := make([]int, n)
	left, right := 0, -1
	for i := 0; i < n; i++ {
		radius := 1
		if i <= right {
			mirror := left + right - i
			radius = odd[mirror]
			if right-i+1 < radius {
				radius = right - i + 1
			}
		}
		for i-radius >= 0 && i+radius < n && nums[i-radius] == nums[i+radius] {
			radius++
		}
		odd[i] = radius
		if i+radius-1 > right {
			left, right = i-radius+1, i+radius-1
		}
	}
	even := make([]int, n)
	left, right = 0, -1
	for i := 0; i < n; i++ {
		radius := 0
		if i <= right {
			mirror := left + right - i + 1
			radius = even[mirror]
			if right-i+1 < radius {
				radius = right - i + 1
			}
		}
		for i-radius-1 >= 0 && i+radius < n && nums[i-radius-1] == nums[i+radius] {
			radius++
		}
		even[i] = radius
		if i+radius-1 > right {
			left, right = i-radius, i+radius-1
		}
	}
	var answer int64
	for i := 0; i < n; i++ {
		sum := prefix[i+odd[i]] - prefix[i-odd[i]+1]
		if sum > answer {
			answer = sum
		}
		if even[i] > 0 {
			sum = prefix[i+even[i]] - prefix[i-even[i]]
			if sum > answer {
				answer = sum
			}
		}
	}
	return answer
}