<?php
// LeetCode 3663 - Find The Least Frequent Digit
// https://leetcode.com/problems/find-the-least-frequent-digit/

class Solution {
    function getLeastFrequentDigit($n) {
        $cnt = array_fill(0, 10, 0);
        $ans = 0;
        $f = 1 << 30;
        for (; $n > 0; $n = intdiv($n, 10)) $cnt[$n % 10]++;
        for ($x = 0; $x < 10; $x++) {
            if ($cnt[$x] > 0 && $cnt[$x] < $f) {
                $f = $cnt[$x];
                $ans = $x;
            }
        }
        return $ans;
    }
}
