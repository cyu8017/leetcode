<?php
// LeetCode 2231 - Largest Number After Digit Swaps by Parity
// https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

class Solution {
    function largestInteger($num) {
        $digits = array_map('intval', str_split((string)$num));
        $even = [];
        $odd = [];
        foreach ($digits as $d) {
            if ($d % 2 === 0) $even[] = $d;
            else $odd[] = $d;
        }
        rsort($even);
        rsort($odd);
        $ei = 0;
        $oi = 0;
        $ans = 0;
        foreach ($digits as $d) {
            if ($d % 2 === 0) $ans = $ans * 10 + $even[$ei++];
            else $ans = $ans * 10 + $odd[$oi++];
        }
        return $ans;
    }
}
