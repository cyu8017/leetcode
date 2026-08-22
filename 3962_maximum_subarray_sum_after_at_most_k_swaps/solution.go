// LeetCode 3962 - Maximum Subarray Sum After at Most K Swaps
// https://leetcode.com/problems/maximum-subarray-sum-after-at-most-k-swaps/

import "sort"

func maxSubarraySum(nums []int, k int) int64 {
	n := len(nums)
	values := append([]int(nil), nums...)
	sort.Ints(values)
	unique := values[:0]
	for _, value := range values {
		if len(unique) == 0 || unique[len(unique)-1] != value {
			unique = append(unique, value)
		}
	}
	rank := make([]int, n)
	globalCount := make([]int, len(unique)+1)
	globalSum := make([]int64, len(unique)+1)
	add := func(count []int, sum []int64, index, delta int) {
		value := int64(unique[index-1])
		for index < len(count) {
			count[index] += delta
			sum[index] += int64(delta) * value
			index += index & -index
		}
	}
	for i, value := range nums {
		rank[i] = sort.SearchInts(unique, value) + 1
		add(globalCount, globalSum, rank[i], 1)
	}
	queryCount := func(bit []int, index int) int {
		result := 0
		for index > 0 {
			result += bit[index]
			index -= index & -index
		}
		return result
	}
	querySum := func(bit []int64, index int) int64 {
		var result int64
		for index > 0 {
			result += bit[index]
			index -= index & -index
		}
		return result
	}
	kth := func(bit []int, order int) int {
		index, step := 0, 1
		for step<<1 < len(bit) {
			step <<= 1
		}
		for ; step > 0; step >>= 1 {
			next := index + step
			if next < len(bit) && bit[next] < order {
				index = next
				order -= bit[next]
			}
		}
		return index + 1
	}
	sumSmallest := func(count []int, sum []int64, amount int) int64 {
		if amount <= 0 {
			return 0
		}
		index := kth(count, amount)
		countBefore := queryCount(count, index-1)
		sumBefore := querySum(sum, index-1)
		return sumBefore + int64(amount-countBefore)*int64(unique[index-1])
	}
	const negativeInfinity int64 = -1 << 60
	answer := negativeInfinity
	for left := 0; left < n; left++ {
		insideCount := make([]int, len(unique)+1)
		insideSum := make([]int64, len(unique)+1)
		outsideCount := append([]int(nil), globalCount...)
		outsideSum := append([]int64(nil), globalSum...)
		var subarraySum int64
		for right := left; right < n; right++ {
			add(outsideCount, outsideSum, rank[right], -1)
			add(insideCount, insideSum, rank[right], 1)
			subarraySum += int64(nums[right])
			insideSize := right - left + 1
			outsideSize := n - insideSize
			limit := k
			if insideSize < limit {
				limit = insideSize
			}
			if outsideSize < limit {
				limit = outsideSize
			}
			low, high := 0, limit
			for low < high {
				mid := (low + high + 1) / 2
				insideValue := unique[kth(insideCount, mid)-1]
				outsideOrder := outsideSize - mid + 1
				outsideValue := unique[kth(outsideCount, outsideOrder)-1]
				if outsideValue > insideValue {
					low = mid
				} else {
					high = mid - 1
				}
			}
			swaps := low
			gain := int64(0)
			if swaps > 0 {
				smallInside := sumSmallest(insideCount, insideSum, swaps)
				totalOutside := querySum(outsideSum, len(unique))
				largeOutside := totalOutside - sumSmallest(outsideCount, outsideSum, outsideSize-swaps)
				gain = largeOutside - smallInside
			}
			if subarraySum+gain > answer {
				answer = subarraySum + gain
			}
		}
	}
	return answer
}