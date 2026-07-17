// LeetCode 1712 - Ways to Split Array Into Three Subarrays
// https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/

func waysToSplit(nums []int) int {
	const mod = 1000000007
	n := len(nums)
	prefix := make([]int64, n)
	var total int64
	for i, v := range nums {
		total += int64(v)
		prefix[i] = total
	}

	lowerBound := func(target int64, lo, hi int) int {
		for lo < hi {
			mid := (lo + hi) / 2
			if prefix[mid] < target {
				lo = mid + 1
			} else {
				hi = mid
			}
		}
		return lo
	}

	upperBound := func(target int64, lo, hi int) int {
		for lo < hi {
			mid := (lo + hi) / 2
			if prefix[mid] <= target {
				lo = mid + 1
			} else {
				hi = mid
			}
		}
		return lo
	}

	ans := 0
	for i := 0; i < n-2; i++ {
		left := prefix[i]
		lo := lowerBound(2*left, i+1, n-1)
		hi := upperBound((total+left)/2, lo, n-1)
		ans = (ans + hi - lo) % mod
	}
	return ans
}
