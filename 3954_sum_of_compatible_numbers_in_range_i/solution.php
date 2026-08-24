<?php
// LeetCode 3954 - Sum Of Compatible Numbers In Range I
// https://leetcode.com/problems/sum-of-compatible-numbers-in-range-i/

class Solution {
    function sumOfGoodIntegers($n, $k) {
        $start = max(1, $n - $k);
        $end = $n + $k;
        $ans = 0;
        for ($x = $start; $x <= $end; $x++) {
            if (($n & $x) == 0) $ans += $x;
        }
        return $ans;
    }
}
