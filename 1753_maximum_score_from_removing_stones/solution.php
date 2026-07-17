<?php
// LeetCode 1753 - Maximum Score From Removing Stones
// https://leetcode.com/problems/maximum-score-from-removing-stones/

class Solution {
    /**
     * @param Integer $a
     * @param Integer $b
     * @param Integer $c
     * @return Integer
     */
    function maximumScore($a, $b, $c) {
        $stones = [$a, $b, $c];
        rsort($stones);
        $score = 0;
        while ($stones[0] > 0 && $stones[1] > 0) {
            $stones[0]--;
            $stones[1]--;
            $score++;
            rsort($stones);
        }
        return $score;
    }
}
