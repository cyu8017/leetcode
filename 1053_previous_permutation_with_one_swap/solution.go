// LeetCode 1053 - Previous Permutation With One Swap
// https://leetcode.com/problems/previous-permutation-with-one-swap/

func prevPermOpt1(arr []int) []int {
	n := len(arr)
	i := n - 2
	for i >= 0 && arr[i] <= arr[i+1] {
		i--
	}
	if i < 0 {
		return arr
	}
	j := n - 1
	for arr[j] >= arr[i] || arr[j] == arr[j-1] {
		j--
	}
	arr[i], arr[j] = arr[j], arr[i]
	return arr
}
