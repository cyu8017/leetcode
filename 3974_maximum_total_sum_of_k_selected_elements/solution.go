// LeetCode 3974 - Maximum Total Sum Of K Selected Elements
// https://leetcode.com/problems/maximum-total-sum-of-k-selected-elements/

import "sort"

func maxSum(nums []int, k int, mul int) int64 {
    sort.Ints(nums)
    n := len(nums)
    var ans int64 = 0

    for i := n - 1; i >= n-k; i-- {
        m := max(1, mul)
        ans += int64(nums[i]) * int64(m)
        mul--
    }

    return ans
}
