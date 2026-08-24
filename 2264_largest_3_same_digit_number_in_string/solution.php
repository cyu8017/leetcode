<?php
// LeetCode 2264 - Largest 3-Same-Digit Number in String
// https://leetcode.com/problems/largest-3-same-digit-number-in-string/

class Solution {
    function largestGoodInteger($num) {
        $best = '';
        $n = strlen($num);
        for ($i = 0; $i + 2 < $n; $i++) {
            if ($num[$i] === $num[$i + 1] && $num[$i] === $num[$i + 2]) {
                $cand = substr($num, $i, 3);
                if ($cand > $best) $best = $cand;
            }
        }
        return $best;
    }
}
