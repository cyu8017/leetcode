<?php
// LeetCode 0202 - Happy Number
// https://leetcode.com/problems/happy-number/

class Solution {
    function isHappy($n) {
        $seen = [];
        while ($n !== 1 && !isset($seen[$n])) {
            $seen[$n] = true;
            $total = 0;
            while ($n > 0) {
                $digit = $n % 10;
                $total += $digit * $digit;
                $n = intdiv($n, 10);
            }
            $n = $total;
        }
        return $n === 1;
    }
}
