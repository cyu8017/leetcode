<?php
// LeetCode 0747 - Largest Number At Least Twice of Others
// https://leetcode.com/problems/largest-number-at-least-twice-of-others/

class Solution {
    function dominantIndex($nums) {
        $first = -1;
        $second = -1;
        $index = -1;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] > $first) { $second = $first; $first = $nums[$i]; $index = $i; }
            else if ($nums[$i] > $second) $second = $nums[$i];
        }
        return $first >= 2 * $second ? $index : -1;
    }
}
