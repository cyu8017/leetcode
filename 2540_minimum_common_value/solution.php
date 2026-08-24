<?php
// LeetCode 2540 - Minimum Common Value
// https://leetcode.com/problems/minimum-common-value/

class Solution {
    function getCommon($nums1, $nums2) {
        $i = 0;
        $j = 0;
        $n1 = count($nums1);
        $n2 = count($nums2);
        while ($i < $n1 && $j < $n2) {
            if ($nums1[$i] === $nums2[$j]) return $nums1[$i];
            if ($nums1[$i] < $nums2[$j]) $i++;
            else $j++;
        }
        return -1;
    }
}
