<?php
// LeetCode 0828 - Count Unique Characters of All Substrings of a Given String
// https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function uniqueLetterString($s) {
        $n = strlen($s);
        $last = [];
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            if (!isset($last[$ch])) $last[$ch] = [-1];
        }
        for ($i = 0; $i < $n; $i++) $last[$s[$i]][] = $i;
        foreach ($last as $ch => $_) $last[$ch][] = $n;
        $ans = 0;
        foreach ($last as $indices) {
            $len = count($indices);
            for ($k = 1; $k + 1 < $len; $k++) {
                $ans += ($indices[$k] - $indices[$k - 1]) * ($indices[$k + 1] - $indices[$k]);
            }
        }
        return $ans;
    }
}
