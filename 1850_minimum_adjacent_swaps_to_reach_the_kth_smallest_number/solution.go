// LeetCode 1850 - Minimum Adjacent Swaps to Reach the Kth Smallest Number
// https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/

func getMinSwaps(num string, k int) int {
	target := []byte(num)
	for i := 0; i < k; i++ {
		nextPermutationBytes(target)
	}

	source := []byte(num)
	swaps := 0
	for i := range source {
		if source[i] == target[i] {
			continue
		}

		j := i
		for source[j] != target[i] {
			j++
		}
		for j > i {
			source[j], source[j-1] = source[j-1], source[j]
			swaps++
			j--
		}
	}

	return swaps
}

func nextPermutationBytes(arr []byte) {
	i := len(arr) - 2
	for i >= 0 && arr[i] >= arr[i+1] {
		i--
	}
	if i < 0 {
		reverseBytes(arr)
		return
	}

	j := len(arr) - 1
	for arr[j] <= arr[i] {
		j--
	}
	arr[i], arr[j] = arr[j], arr[i]
	reverseBytes(arr[i+1:])
}

func reverseBytes(arr []byte) {
	for left, right := 0, len(arr)-1; left < right; left, right = left+1, right-1 {
		arr[left], arr[right] = arr[right], arr[left]
	}
}
