<?php
// LeetCode 0274 - H-Index
// https://leetcode.com/problems/h-index/

class Solution {
    /**
     * @param Integer[] $citations
     * @return Integer
     */
    function hIndex($citations) {
        $buckets = array_fill(0, count($citations) + 1, 0);
        foreach ($citations as $citation) {
            $index = min($citation, count($citations));
            $buckets[$index]++;
        }
        $total = 0;
        for ($h = count($buckets) - 1; $h >= 0; $h--) {
            $total += $buckets[$h];
            if ($total >= $h) {
                return $h;
            }
        }
        return 0;
    }
}
