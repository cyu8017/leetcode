// LeetCode 0327 - Count of Range Sum
// https://leetcode.com/problems/count-of-range-sum/

func countRangeSum(nums []int, lower int, upper int) int {
	prefix := make([]int64, 0, len(nums)+1)
	prefix = append(prefix, 0)
	for _, num := range nums {
		prefix = append(prefix, prefix[len(prefix)-1]+int64(num))
	}
	temp := make([]int64, len(prefix))

	var mergeSort func(left int, right int) int
	mergeSort = func(left int, right int) int {
		if left >= right {
			return 0
		}
		mid := left + (right-left)/2
		count := mergeSort(left, mid) + mergeSort(mid+1, right)
		start, end := mid+1, mid+1
		for index := left; index <= mid; index++ {
			for start <= right && prefix[start]-prefix[index] < int64(lower) {
				start++
			}
			for end <= right && prefix[end]-prefix[index] <= int64(upper) {
				end++
			}
			count += end - start
		}
		tempLeft, tempRight, write := left, mid+1, left
		for tempLeft <= mid && tempRight <= right {
			if prefix[tempLeft] <= prefix[tempRight] {
				temp[write] = prefix[tempLeft]
				tempLeft++
			} else {
				temp[write] = prefix[tempRight]
				tempRight++
			}
			write++
		}
		for tempLeft <= mid {
			temp[write] = prefix[tempLeft]
			tempLeft++
			write++
		}
		for tempRight <= right {
			temp[write] = prefix[tempRight]
			tempRight++
			write++
		}
		copy(prefix[left:right+1], temp[left:right+1])
		return count
	}

	return mergeSort(0, len(prefix)-1)
}
