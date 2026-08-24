<?php
// LeetCode 0349 - Intersection of Two Arrays
// https://leetcode.com/problems/intersection-of-two-arrays/

class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer[]
     */
    function intersection($nums1, $nums2) {
        $set2 = array_fill_keys($nums2, true);
        $seen = [];
        $result = [];

        foreach ($nums1 as $num) {
            if (isset($set2[$num]) && !isset($seen[$num])) {
                $seen[$num] = true;
                $result[] = $num;
            }
        }

        return $result;
    }
}
