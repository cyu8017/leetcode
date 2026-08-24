<?php
// LeetCode 4000 - Largest Integer With Given Digit Sum
// https://leetcode.com/problems/largest-integer-with-given-digit-sum/

class Solution {
    function largestInteger($n, $s) {
        if ($n * 9 < $s) return -1;
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $x = $s < 9 ? $s : 9;
            $ans = $ans * 10 + $x;
            $s -= $x;
        }
        return $ans;
    }
}
