// LeetCode 1856 - Maximum Subarray Min-Product
// https://leetcode.com/problems/maximum-subarray-min-product/

func maxSumMinProduct(nums []int) int {
	const mod = 1000000007
	n := len(nums)
	prefix := make([]int, n+1)
	for index, value := range nums {
		prefix[index+1] = prefix[index] + value
	}

	leftBound := make([]int, n)
	stack := []int{}
	for index, value := range nums {
		for len(stack) > 0 && nums[stack[len(stack)-1]] >= value {
			stack = stack[:len(stack)-1]
		}
		if len(stack) > 0 {
			leftBound[index] = stack[len(stack)-1]
		} else {
			leftBound[index] = -1
		}
		stack = append(stack, index)
	}

	rightBound := make([]int, n)
	stack = stack[:0]
	for index := n - 1; index >= 0; index-- {
		value := nums[index]
		for len(stack) > 0 && nums[stack[len(stack)-1]] >= value {
			stack = stack[:len(stack)-1]
		}
		if len(stack) > 0 {
			rightBound[index] = stack[len(stack)-1]
		} else {
			rightBound[index] = n
		}
		stack = append(stack, index)
	}

	best := 0
	for index, value := range nums {
		total := prefix[rightBound[index]] - prefix[leftBound[index]+1]
		candidate := total * value
		if candidate > best {
			best = candidate
		}
	}

	return best % mod
}
