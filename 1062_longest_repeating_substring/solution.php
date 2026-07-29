<?php
// LeetCode 1062 - Longest Repeating Substring
// https://leetcode.com/problems/longest-repeating-substring/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function longestRepeatingSubstring($s) {
        $n = strlen($s);
        $hasDup = function ($length) use ($s, $n) {
            $seen = [];
            for ($i = 0; $i <= $n - $length; $i++) {
                $sub = substr($s, $i, $length);
                if (isset($seen[$sub])) {
                    return true;
                }
                $seen[$sub] = true;
            }
            return false;
        };
        $lo = 1;
        $hi = $n - 1;
        $ans = 0;
        while ($lo <= $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($hasDup($mid)) {
                $ans = $mid;
                $lo = $mid + 1;
            } else {
                $hi = $mid - 1;
            }
        }
        return $ans;
    }
}
