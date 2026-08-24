<?php
// LeetCode 3931 - Check Adjacent Digit Differences
// https://leetcode.com/problems/check-adjacent-digit-differences/

class Solution {
    function isAdjacentDiffAtMostTwo($s) {
        $n = strlen($s);
        for ($i = 1; $i < $n; $i++) {
            if (abs(intval($s[$i - 1]) - intval($s[$i])) > 2) return false;
        }
        return true;
    }
}
