<?php
// LeetCode 1781 - Sum of Beauty of All Substrings
// https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function beautySum($s) {
        $n = strlen($s);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $freq = array_fill(0, 26, 0);
            for ($j = $i; $j < $n; $j++) {
                $freq[ord($s[$j]) - 97]++;
                $lo = PHP_INT_MAX;
                $hi = 0;
                foreach ($freq as $count) {
                    if ($count > 0) {
                        $lo = min($lo, $count);
                        $hi = max($hi, $count);
                    }
                }
                $ans += $hi - $lo;
            }
        }
        return $ans;
    }
}
