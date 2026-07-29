<?php
// LeetCode 1010 - Pairs of Songs With Total Durations Divisible by 60
// https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

class Solution {
    /**
     * @param Integer[] $time
     * @return Integer
     */
    function numPairsDivisibleBy60($time) {
        $count = array_fill(0, 60, 0);
        $ans = 0;
        foreach ($time as $t) {
            $ans += $count[(60 - $t % 60) % 60];
            $count[$t % 60]++;
        }
        return $ans;
    }
}
