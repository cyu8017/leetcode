<?php

class Solution {
    /**
     * @param String $colors
     * @param Integer[] $neededTime
     * @return Integer
     */
    function minCost($colors, $neededTime) {
        $answer = 0;
        $maximum = 0;
        $n = count($neededTime);
        for ($i = 0; $i < $n; $i++) {
            $cost = $neededTime[$i];
            if ($i > 0 && $colors[$i] !== $colors[$i - 1]) {
                $maximum = 0;
            }
            $answer += min($maximum, $cost);
            $maximum = max($maximum, $cost);
        }
        return $answer;
    }
}
