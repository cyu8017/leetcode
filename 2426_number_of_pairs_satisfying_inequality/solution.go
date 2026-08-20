// LeetCode 2426 - Number of Pairs Satisfying Inequality
// https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

func numberOfPairs(nums1 []int, nums2 []int, diff int) int64 {
	n := len(nums1)
	arr := make([]int, n)
	for i := 0; i < n; i++ {
		arr[i] = nums1[i] - nums2[i]
	}
	tmp := make([]int, n)
	var mergeCount func(int, int) int64
	mergeCount = func(l, r int) int64 {
		if r-l <= 1 {
			return 0
		}
		m := (l + r) / 2
		ans := mergeCount(l, m) + mergeCount(m, r)
		j := m
		for i := l; i < m; i++ {
			for j < r && arr[j] < arr[i]-diff {
				j++
			}
			ans += int64(r - j)
		}
		i, p, q := l, l, m
		for p < m && q < r {
			if arr[p] <= arr[q] {
				tmp[i] = arr[p]
				p++
			} else {
				tmp[i] = arr[q]
				q++
			}
			i++
		}
		for p < m {
			tmp[i] = arr[p]
			p++
			i++
		}
		for q < r {
			tmp[i] = arr[q]
			q++
			i++
		}
		copy(arr[l:r], tmp[l:r])
		return ans
	}
	return mergeCount(0, n)
}
