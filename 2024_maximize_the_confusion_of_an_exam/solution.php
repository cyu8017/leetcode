<?php
// LeetCode 2024 - Maximize the Confusion of an Exam
// https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

class Solution {
    /**
     * @param String $answerKey
     * @param Integer $k
     * @return Integer
     */
    function maxConsecutiveAnswers($answerKey, $k) {
        $maxWith = function ($ch) use ($answerKey, $k) {
            $left = 0;
            $bad = 0;
            $best = 0;
            $n = strlen($answerKey);
            for ($right = 0; $right < $n; $right++) {
                if ($answerKey[$right] !== $ch) $bad++;
                while ($bad > $k) {
                    if ($answerKey[$left] !== $ch) $bad--;
                    $left++;
                }
                $best = max($best, $right - $left + 1);
            }
            return $best;
        };
        return max($maxWith('T'), $maxWith('F'));
    }
}
