<?php
// LeetCode 2644 - Find the Maximum Divisibility Score
// https://leetcode.com/problems/find-the-maximum-divisibility-score/

class Solution {
    function maxDivScore($nums, $divisors) {
        $best = $divisors[0];
        $bestScore = -1;
        foreach ($divisors as $d) {
            $score = 0;
            foreach ($nums as $x) if ($x % $d === 0) $score++;
            if ($score > $bestScore || ($score === $bestScore && $d < $best)) {
                $bestScore = $score;
                $best = $d;
            }
        }
        return $best;
    }
}
