// LeetCode 0004 - Median of Two Sorted Arrays
// https://leetcode.com/problems/median-of-two-sorted-arrays/

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	if len(nums1) > len(nums2) {
		nums1, nums2 = nums2, nums1
	}

	m, n := len(nums1), len(nums2)
	totalLeft := (m + n + 1) / 2
	lo, hi := 0, m

	for lo <= hi {
		i := (lo + hi) / 2
		j := totalLeft - i

		nums1LeftMax := mathMinInt
		if i > 0 {
			nums1LeftMax = nums1[i-1]
		}
		nums1RightMin := mathMaxInt
		if i < m {
			nums1RightMin = nums1[i]
		}
		nums2LeftMax := mathMinInt
		if j > 0 {
			nums2LeftMax = nums2[j-1]
		}
		nums2RightMin := mathMaxInt
		if j < n {
			nums2RightMin = nums2[j]
		}

		if nums1LeftMax <= nums2RightMin && nums2LeftMax <= nums1RightMin {
			if (m+n)%2 == 1 {
				return float64(max(nums1LeftMax, nums2LeftMax))
			}
			return float64(max(nums1LeftMax, nums2LeftMax)+min(nums1RightMin, nums2RightMin)) / 2.0
		}

		if nums1LeftMax > nums2RightMin {
			hi = i - 1
		} else {
			lo = i + 1
		}
	}

	return 0
}

const mathMinInt = -1 << 30
const mathMaxInt = 1<<31 - 1

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
