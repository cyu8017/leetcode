<?php
// LeetCode 2272 - Substring With Largest Variance
// https://leetcode.com/problems/substring-with-largest-variance/

class Solution {
    function largestVariance($s) {
        $ans = 0;
        $n = strlen($s);
        for ($ai = 0; $ai < 26; $ai++) {
            for ($bi = 0; $bi < 26; $bi++) {
                if ($ai === $bi) continue;
                $a = chr(97 + $ai);
                $b = chr(97 + $bi);
                $bal = 0;
                $hasB = false;
                for ($i = 0; $i < $n; $i++) {
                    $c = $s[$i];
                    if ($c === $a) $bal++;
                    else if ($c === $b) { $bal--; $hasB = true; }
                    if ($hasB) $ans = max($ans, $bal);
                    if ($bal < 0) { $bal = 0; $hasB = false; }
                }
            }
        }
        return $ans;
    }
}
