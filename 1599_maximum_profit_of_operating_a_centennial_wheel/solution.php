<?php

class Solution {
    /**
     * @param Integer[] $customers
     * @param Integer $boardingCost
     * @param Integer $runningCost
     * @return Integer
     */
    function minOperationsMaxProfit($customers, $boardingCost, $runningCost) {
        $waiting = 0;
        $profit = 0;
        $best = 0;
        $answer = 0;
        $rotation = 0;
        $i = 0;
        $n = count($customers);
        while ($i < $n || $waiting > 0) {
            if ($i < $n) {
                $waiting += $customers[$i];
            }
            $boarded = min(4, $waiting);
            $waiting -= $boarded;
            $rotation++;
            $profit += $boarded * $boardingCost - $runningCost;
            if ($profit > $best) {
                $best = $profit;
                $answer = $rotation;
            }
            $i++;
        }
        return $best > 0 ? $answer : -1;
    }
}
