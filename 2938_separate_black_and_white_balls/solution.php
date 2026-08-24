<?php
// LeetCode 2938 - Separate Black and White Balls
// https://leetcode.com/problems/separate-black-and-white-balls/

class Solution {
    function minimumSteps($s) {
        $ans = 0;
        $zeros = 0;
        for ($i = strlen($s) - 1; $i >= 0; $i--) {
            if ($s[$i] === '0') $zeros++;
            else $ans += $zeros;
        }
        return $ans;
    }
}
