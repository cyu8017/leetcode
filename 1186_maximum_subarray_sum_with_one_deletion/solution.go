// LeetCode 1186 - Maximum Subarray Sum with One Deletion
// https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

func maximumSum(arr []int) int {
	keep, delete, ans := arr[0], arr[0], arr[0]
	for i := 1; i < len(arr); i++ {
		x := arr[i]
		nd := keep
		if delete+x > nd {
			nd = delete + x
		}
		nk := keep + x
		if x > nk {
			nk = x
		}
		keep, delete = nk, nd
		if keep > ans {
			ans = keep
		}
		if delete > ans {
			ans = delete
		}
	}
	return ans
}
