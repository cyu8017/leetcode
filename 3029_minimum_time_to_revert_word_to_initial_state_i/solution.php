<?php
// LeetCode 3029 - Minimum Time to Revert Word to Initial State I
// https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-i/

class Solution {
    function minimumTimeToInitialState($word, $k) {
        $n = strlen($word);
        for ($i = $k; $i < $n; $i += $k) {
            if (substr($word, $i) === substr($word, 0, $n - $i)) return intdiv($i, $k);
        }
        return intdiv($n + $k - 1, $k);
    }
}
