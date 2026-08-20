// LeetCode 2035 - Partition Array Into Two Arrays to Minimize Sum Difference
// https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/

import "sort"

func minimumDifference(nums []int) int {
	n := len(nums) / 2
	total := 0
	for _, v := range nums {
		total += v
	}
	left, right := nums[:n], nums[n:]
	sumsByCount := func(arr []int) [][]int {
		m := len(arr)
		res := make([][]int, m+1)
		for mask := 0; mask < 1<<m; mask++ {
			sum, c := 0, 0
			for i := 0; i < m; i++ {
				if mask&(1<<i) != 0 {
					sum += arr[i]
					c++
				}
			}
			res[c] = append(res[c], sum)
		}
		for i := range res {
			sort.Ints(res[i])
		}
		return res
	}
	L := sumsByCount(left)
	R := sumsByCount(right)
	ans := int(1e18)
	for k := 0; k <= n; k++ {
		for _, s1 := range L[k] {
			need := total/2 - s1
			arr := R[n-k]
			j := sort.SearchInts(arr, need)
			for _, idx := range []int{j - 1, j} {
				if idx >= 0 && idx < len(arr) {
					s2 := arr[idx]
					diff := total - 2*(s1+s2)
					if diff < 0 {
						diff = -diff
					}
					if diff < ans {
						ans = diff
					}
				}
			}
		}
	}
	return ans
}
