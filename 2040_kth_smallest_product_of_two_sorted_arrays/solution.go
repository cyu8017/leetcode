// LeetCode 2040 - Kth Smallest Product of Two Sorted Arrays
// https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/

func kthSmallestProduct(nums1 []int, nums2 []int, k int64) int64 {
	countLE := func(x int64) int64 {
		var cnt int64
		for _, a := range nums1 {
			if a > 0 {
				lo, hi := 0, len(nums2)
				for lo < hi {
					mid := (lo + hi) / 2
					if int64(a)*int64(nums2[mid]) <= x {
						lo = mid + 1
					} else {
						hi = mid
					}
				}
				cnt += int64(lo)
			} else if a < 0 {
				lo, hi := 0, len(nums2)
				for lo < hi {
					mid := (lo + hi) / 2
					if int64(a)*int64(nums2[mid]) <= x {
						hi = mid
					} else {
						lo = mid + 1
					}
				}
				cnt += int64(len(nums2) - lo)
			} else if x >= 0 {
				cnt += int64(len(nums2))
			}
		}
		return cnt
	}
	lo, hi := int64(-1e10), int64(1e10)
	for lo < hi {
		mid := lo + (hi-lo)/2
		if countLE(mid) >= k {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}
