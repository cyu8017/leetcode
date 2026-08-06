<?php

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function getMaxLen($nums) {
        $positive = 0;
        $negative = 0;
        $answer = 0;
        foreach ($nums as $x) {
            if ($x === 0) {
                $positive = 0;
                $negative = 0;
            } elseif ($x > 0) {
                $positive++;
                $negative = $negative ? $negative + 1 : 0;
            } else {
                $newPositive = $negative ? $negative + 1 : 0;
                $negative = $positive + 1;
                $positive = $newPositive;
            }
            $answer = max($answer, $positive);
        }
        return $answer;
    }
}
