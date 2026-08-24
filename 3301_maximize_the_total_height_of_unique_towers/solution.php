<?php
// LeetCode 3301 - Maximize the Total Height of Unique Towers
// https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/

class Solution {
    function maximumTotalSum($maximumHeight) {
        rsort($maximumHeight);
        $ans = 0;
        $prev = 1e18;
        foreach ($maximumHeight as $h) {
            $cur = $h;
            if ($cur >= $prev) $cur = $prev - 1;
            if ($cur <= 0) return -1;
            $ans += $cur;
            $prev = $cur;
        }
        return $ans;
    }
}
