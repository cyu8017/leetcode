<?php
// LeetCode 1100 - Find K-Length Substrings With No Repeated Characters
// https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/

class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function numKLenSubstrNoRepeats($s, $k) {
        $n = strlen($s);
        if ($k > $n) return 0;
        $window = [];
        for ($i = 0; $i < $k; $i++) {
            $ch = $s[$i];
            $window[$ch] = ($window[$ch] ?? 0) + 1;
        }
        $ans = count($window) === $k ? 1 : 0;
        for ($i = $k; $i < $n; $i++) {
            $ch = $s[$i];
            $window[$ch] = ($window[$ch] ?? 0) + 1;
            $left = $s[$i - $k];
            $window[$left]--;
            if ($window[$left] === 0) unset($window[$left]);
            if (count($window) === $k) $ans++;
        }
        return $ans;
    }
}
