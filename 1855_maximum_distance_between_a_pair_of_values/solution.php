<?php
// LeetCode 1855 - Maximum Distance Between a Pair of Values
// https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function maxDistance($nums1, $nums2) {
        $answer = 0;
        $j = 0;
        $n2 = count($nums2);

        foreach ($nums1 as $i => $value) {
            while ($j < $n2 && $value <= $nums2[$j]) {
                $j++;
            }
            $answer = max($answer, $j - $i - 1);
        }

        return $answer;
    }
}
