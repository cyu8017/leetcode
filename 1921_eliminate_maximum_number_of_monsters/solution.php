<?php
// LeetCode 1921 - Eliminate Maximum Number of Monsters
// https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

class Solution {
    /**
     * @param Integer[] $dist
     * @param Integer[] $speed
     * @return Integer
     */
    function eliminateMaximum($dist, $speed) {
        $n = count($dist);
        $arrival = [];
        for ($i = 0; $i < $n; $i++) {
            $arrival[] = intdiv($dist[$i] + $speed[$i] - 1, $speed[$i]);
        }
        sort($arrival);
        for ($i = 0; $i < $n; $i++) {
            if ($arrival[$i] <= $i) {
                return $i;
            }
        }
        return $n;
    }
}
