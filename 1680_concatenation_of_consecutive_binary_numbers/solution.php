<?php
// LeetCode 1680 - Concatenation of Consecutive Binary Numbers
// https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

class Solution {
    function concatenatedBinary($n) {
        $ans = 0;
        $bits = 0;
        $mod = 1000000007;
        for ($x = 1; $x <= $n; $x++) {
            if (($x & ($x - 1)) === 0) $bits++;
            $ans = (($ans << $bits) % $mod + $x) % $mod;
        }
        return $ans;
    }
}
