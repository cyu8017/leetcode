<?php
// LeetCode 3397 - Maximum Number of Distinct Elements After Operations
// https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/

class Solution {
    function maxDistinctElements($nums, $k) {
        sort($nums);
        $ans = 0;
        $prev = PHP_INT_MIN / 2;
        foreach ($nums as $x) {
            $cur = $x - $k;
            if ($cur <= $prev) $cur = $prev + 1;
            if ($cur > $x + $k) continue;
            $ans++;
            $prev = $cur;
        }
        return $ans;
    }
}
