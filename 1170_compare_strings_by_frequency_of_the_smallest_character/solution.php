<?php
// LeetCode 1170 - Compare Strings by Frequency of the Smallest Character
// https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

class Solution {
    /**
     * @param String[] $queries
     * @param String[] $words
     * @return Integer[]
     */
    function numSmallerByFrequency($queries, $words) {
        $f = function ($s) {
            $min = min(str_split($s));
            return substr_count($s, $min);
        };
        $freqs = array_map($f, $words);
        sort($freqs);
        $ans = [];
        foreach ($queries as $q) {
            $fq = $f($q);
            $lo = 0; $hi = count($freqs);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($freqs[$mid] <= $fq) $lo = $mid + 1;
                else $hi = $mid;
            }
            $ans[] = count($freqs) - $lo;
        }
        return $ans;
    }
}
