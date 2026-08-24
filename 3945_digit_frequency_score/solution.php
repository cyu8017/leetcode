<?php
// LeetCode 3945 - Digit Frequency Score
// https://leetcode.com/problems/digit-frequency-score/

class Solution {
    function digitFrequencyScore($n) {
        $ans = 0;
        for (; $n > 0; $n = intdiv($n, 10)) $ans += $n % 10;
        return $ans;
    }
}
