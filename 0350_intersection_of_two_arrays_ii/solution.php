<?php
// LeetCode 0350 - Intersection of Two Arrays II
// https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer[]
     */
    function intersect($nums1, $nums2) {
        $counts = [];
        foreach ($nums1 as $num) {
            if (!array_key_exists($num, $counts)) {
                $counts[$num] = 0;
            }
            $counts[$num]++;
        }

        $result = [];
        foreach ($nums2 as $num) {
            if (($counts[$num] ?? 0) > 0) {
                $result[] = $num;
                $counts[$num]--;
            }
        }

        return $result;
    }
}
