<?php
// LeetCode 1686 - Stone Game VI
// https://leetcode.com/problems/stone-game-vi/

class Solution {
    function stoneGameVI($aliceValues, $bobValues) {
        $n = count($aliceValues);
        $order = range(0, $n - 1);
        usort($order, function($i, $j) use ($aliceValues, $bobValues) {
            return ($bobValues[$j] + $aliceValues[$j]) - ($bobValues[$i] + $aliceValues[$i]);
        });
        $score = 0;
        foreach ($order as $t => $i) {
            $score += ($t % 2 === 0) ? $aliceValues[$i] : -$bobValues[$i];
        }
        return $score <=> 0;
    }
}
