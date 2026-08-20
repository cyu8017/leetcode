// LeetCode 2875 - Minimum Size Subarray in Infinite Array
// https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

func minSizeSubarray(nums []int, target int) int {
	n := len(nums)
	var total int64
	for _, v := range nums {
		total += int64(v)
	}
	ans := 1 << 30
	if total > 0 {
		loops := target / int(total)
		remain := target % int(total)
		if remain == 0 {
			return loops * n
		}
		// find shortest subarray with sum remain in doubled array
		arr := append(append([]int{}, nums...), nums...)
		left := 0
		sum := 0
		best := 1 << 30
		for right := 0; right < len(arr); right++ {
			sum += arr[right]
			for sum > remain && left <= right {
				sum -= arr[left]
				left++
			}
			if sum == remain && right-left+1 < best {
				best = right - left + 1
			}
		}
		if best < 1<<30 {
			ans = loops*n + best
		}
	}
	if ans == 1<<30 {
		return -1
	}
	return ans
}
