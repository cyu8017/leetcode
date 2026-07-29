<?php
// LeetCode 1081 - Smallest Subsequence of Distinct Characters
// https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

class Solution {
    /**
     * @param String $s
     * @return String
     */
    function smallestSubsequence($s) {
        $last = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $last[$s[$i]] = $i;
        }
        $stack = [];
        $used = [];
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            if (isset($used[$ch])) {
                continue;
            }
            while (!empty($stack) && $ch < end($stack) && $last[end($stack)] > $i) {
                unset($used[array_pop($stack)]);
            }
            $stack[] = $ch;
            $used[$ch] = true;
        }
        return implode("", $stack);
    }
}
