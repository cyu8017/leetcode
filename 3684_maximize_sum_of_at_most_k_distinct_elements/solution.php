<?php
// LeetCode 3684 - Maximize Sum of At Most K Distinct Elements
// https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/

class Solution {
    function maxKDistinct($nums, $k) {
        sort($nums);
        $n = count($nums);
        $ans = [];
        for ($i = $n - 1; $i >= 0; $i--) {
            if ($i + 1 < $n && $nums[$i] === $nums[$i + 1]) continue;
            $ans[] = $nums[$i];
            if (--$k === 0) break;
        }
        return $ans;
    }
}
