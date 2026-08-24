<?php
// LeetCode 3682 - Minimum Index Sum of Common Elements
// https://leetcode.com/problems/minimum-index-sum-of-common-elements/

class Solution {
    function minimumSum($nums1, $nums2) {
        $inf = 1 << 30;
        $d = [];
        $n2 = count($nums2);
        for ($i = 0; $i < $n2; $i++)
            if (!isset($d[$nums2[$i]])) $d[$nums2[$i]] = $i;
        $ans = $inf;
        $n1 = count($nums1);
        for ($i = 0; $i < $n1; $i++) {
            if (isset($d[$nums1[$i]])) $ans = min($ans, $i + $d[$nums1[$i]]);
        }
        return $ans === $inf ? -1 : $ans;
    }
}
