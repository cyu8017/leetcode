<?php
// LeetCode 2398 - Maximum Number of Robots Within Budget
// https://leetcode.com/problems/maximum-number-of-robots-within-budget/

class Solution {
    function maximumRobots($chargeTimes, $runningCosts, $budget) {
        $n = count($chargeTimes);
        $left = 0;
        $sum = 0;
        $dq = [];
        $ans = 0;
        for ($right = 0; $right < $n; $right++) {
            while (count($dq) > 0 && $chargeTimes[$dq[count($dq) - 1]] <= $chargeTimes[$right]) array_pop($dq);
            $dq[] = $right;
            $sum += $runningCosts[$right];
            while ($left <= $right && $chargeTimes[$dq[0]] + ($right - $left + 1) * $sum > $budget) {
                if ($dq[0] === $left) array_shift($dq);
                $sum -= $runningCosts[$left];
                $left++;
            }
            $ans = max($ans, $right - $left + 1);
        }
        return $ans;
    }
}
