// LeetCode 1842 - Next Palindrome Using Same Digits
// https://leetcode.com/problems/next-palindrome-using-same-digits/

func nextPalindrome(num string) string {
	nums := []byte(num)
	if !nextPermutationHalf(nums) {
		return ""
	}

	n := len(nums)
	for i := 0; i < n/2; i++ {
		nums[n-i-1] = nums[i]
	}
	return string(nums)
}

func nextPermutationHalf(nums []byte) bool {
	n := len(nums) / 2
	i := n - 2
	for i >= 0 && nums[i] >= nums[i+1] {
		i--
	}
	if i < 0 {
		return false
	}

	j := n - 1
	for nums[j] <= nums[i] {
		j--
	}
	nums[i], nums[j] = nums[j], nums[i]
	reverseBytes(nums[i+1 : n])
	return true
}

func reverseBytes(b []byte) {
	for left, right := 0, len(b)-1; left < right; left, right = left+1, right-1 {
		b[left], b[right] = b[right], b[left]
	}
}
