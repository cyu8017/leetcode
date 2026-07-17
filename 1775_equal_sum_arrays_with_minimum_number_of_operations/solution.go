// LeetCode 1775 - Equal Sum Arrays With Minimum Number of Operations
// https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/

import "sort"

func minOperations(nums1 []int, nums2 []int) int {
    if len(nums1)*6 < len(nums2) || len(nums2)*6 < len(nums1) {
        return -1
    }
    s1, s2 := 0, 0
    for _, x := range nums1 {
        s1 += x
    }
    for _, x := range nums2 {
        s2 += x
    }
    if s1 == s2 {
        return 0
    }
    if s1 < s2 {
        nums1, nums2 = nums2, nums1
        s1, s2 = s2, s1
    }
    diff := s1 - s2
    gains := make([]int, 0, len(nums1)+len(nums2))
    for _, x := range nums1 {
        gains = append(gains, x-1)
    }
    for _, x := range nums2 {
        gains = append(gains, 6-x)
    }
    sort.Sort(sort.Reverse(sort.IntSlice(gains)))
    ops := 0
    for _, gain := range gains {
        if diff <= 0 {
            break
        }
        diff -= gain
        ops++
    }
    if diff <= 0 {
        return ops
    }
    return -1
}
