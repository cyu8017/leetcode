<?php
// LeetCode 3895 - Count Digit Appearances
// https://leetcode.com/problems/count-digit-appearances/

class Solution {
    function countDigitOccurrences($nums, $digit) {
        $ans = 0;
        foreach ($nums as $num) {
            $x = $num;
            for (; $x > 0; $x = intdiv($x, 10)) {
                if ($x % 10 === $digit) $ans++;
            }
        }
        return $ans;
    }
}
