<?php
// LeetCode 3483 - Unique 3-Digit Even Numbers
// https://leetcode.com/problems/unique-3-digit-even-numbers/

class Solution {
    function totalNumbers($digits) {
        $seen = [];
        $n = count($digits);
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($j === $i) continue;
                for ($k = 0; $k < $n; $k++) {
                    if ($k === $i || $k === $j) continue;
                    if ($digits[$i] === 0) continue;
                    if ($digits[$k] % 2 !== 0) continue;
                    $seen[$digits[$i] * 100 + $digits[$j] * 10 + $digits[$k]] = true;
                }
            }
        }
        return count($seen);
    }
}
