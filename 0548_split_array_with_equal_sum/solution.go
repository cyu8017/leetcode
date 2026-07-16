// LeetCode 0548 - Split Array with Equal Sum
// https://leetcode.com/problems/split-array-with-equal-sum/

func splitArray(nums []int) bool {
	n := len(nums)
	if n < 7 {
		return false
	}

	prefix := make([]int64, n+1)
	for index, value := range nums {
		prefix[index+1] = prefix[index] + int64(value)
	}

	for j := 3; j < n-3; j++ {
		seen := make(map[int64]struct{})
		for i := 1; i < j-1; i++ {
			first := prefix[i] - prefix[0]
			second := prefix[j] - prefix[i+1]
			if first == second {
				seen[first] = struct{}{}
			}
		}

		for k := j + 2; k < n-1; k++ {
			third := prefix[k] - prefix[j+1]
			fourth := prefix[n] - prefix[k+1]
			if third == fourth {
				if _, ok := seen[third]; ok {
					return true
				}
			}
		}
	}

	return false
}
