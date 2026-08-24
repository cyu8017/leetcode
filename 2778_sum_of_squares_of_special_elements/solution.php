<?php
// LeetCode 2778 - Sum of Squares of Special Elements
// https://leetcode.com/problems/sum-of-squares-of-special-elements/

class Solution {
    function sumOfSquares($nums) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($n % ($i + 1) === 0) $ans += $nums[$i] * $nums[$i];
        }
        return $ans;
    }
}
