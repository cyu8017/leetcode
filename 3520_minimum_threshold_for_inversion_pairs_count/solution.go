// LeetCode 3520 - Minimum Threshold for Inversion Pairs Count
// https://leetcode.com/problems/minimum-threshold-for-inversion-pairs-count/

func minThreshold(nums []int, k int) int {
	mx := 0
	for _, v := range nums {
		if v > mx {
			mx = v
		}
	}
	l, r := 0, mx+1
	for l < r {
		m := (l + r) / 2
		if countInv(nums, k, m) {
			r = m
		} else {
			l = m + 1
		}
	}
	if l > mx {
		return -1
	}
	return l
}
func countInv(nums []int, k, threshold int) bool {
	sorted := []int{}
	inv := 0
	for _, num := range nums {
		// count values in (num, num+threshold]
		lo, hi := 0, len(sorted)
		for lo < hi {
			mid := (lo + hi) / 2
			if sorted[mid] <= num {
				lo = mid + 1
			} else {
				hi = mid
			}
		}
		left := lo
		lo, hi = 0, len(sorted)
		for lo < hi {
			mid := (lo + hi) / 2
			if sorted[mid] <= num+threshold {
				lo = mid + 1
			} else {
				hi = mid
			}
		}
		inv += lo - left
		// insert num
		lo, hi = 0, len(sorted)
		for lo < hi {
			mid := (lo + hi) / 2
			if sorted[mid] < num {
				lo = mid + 1
			} else {
				hi = mid
			}
		}
		sorted = append(sorted, 0)
		copy(sorted[lo+1:], sorted[lo:])
		sorted[lo] = num
	}
	return inv >= k
}
