<?php
// LeetCode 3314 - Construct the Minimum Bitwise Array I
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

class Solution {
    function minBitwiseArray($nums) {
        $ans = array_fill(0, count($nums), -1);
        for ($i = 0; $i < count($nums); $i++) {
            $n = $nums[$i];
            for ($x = 0; $x < $n; $x++) {
                if (($x | ($x + 1)) === $n) { $ans[$i] = $x; break; }
            }
        }
        return $ans;
    }
}
