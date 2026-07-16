// LeetCode 0321 - Create Maximum Number
// https://leetcode.com/problems/create-maximum-number/

func maxNumber(nums1 []int, nums2 []int, k int) []int {
	pickMax := func(values []int, count int) []int {
		drop := len(values) - count
		stack := make([]int, 0, len(values))
		for _, value := range values {
			for drop > 0 && len(stack) > 0 && stack[len(stack)-1] < value {
				stack = stack[:len(stack)-1]
				drop--
			}
			stack = append(stack, value)
		}
		return stack[:count]
	}

	suffixGreater := func(first []int, left int, second []int, right int) bool {
		for left < len(first) && right < len(second) {
			if first[left] != second[right] {
				return first[left] > second[right]
			}
			left++
			right++
		}
		return len(first)-left > len(second)-right
	}

	merge := func(first []int, second []int) []int {
		result := make([]int, 0, len(first)+len(second))
		left, right := 0, 0
		for left < len(first) && right < len(second) {
			if suffixGreater(first, left, second, right) {
				result = append(result, first[left])
				left++
			} else {
				result = append(result, second[right])
				right++
			}
		}
		result = append(result, first[left:]...)
		result = append(result, second[right:]...)
		return result
	}

	best := []int{}
	minFirst := k - len(nums2)
	if minFirst < 0 {
		minFirst = 0
	}
	maxFirst := k
	if maxFirst > len(nums1) {
		maxFirst = len(nums1)
	}
	for takeFirst := minFirst; takeFirst <= maxFirst; takeFirst++ {
		takeSecond := k - takeFirst
		candidate := merge(pickMax(nums1, takeFirst), pickMax(nums2, takeSecond))
		if len(best) == 0 || compareSlices(candidate, best) > 0 {
			best = candidate
		}
	}
	return best
}

func compareSlices(left []int, right []int) int {
	minLen := len(left)
	if len(right) < minLen {
		minLen = len(right)
	}
	for index := 0; index < minLen; index++ {
		if left[index] != right[index] {
			return left[index] - right[index]
		}
	}
	return len(left) - len(right)
}
