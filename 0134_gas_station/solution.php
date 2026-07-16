<?php

class Solution {
    function canCompleteCircuit($gas, $cost) {
        $total = 0;
        $tank = 0;
        $start = 0;

        foreach ($gas as $i => $amount) {
            $difference = $amount - $cost[$i];
            $total += $difference;
            $tank += $difference;
            if ($tank < 0) {
                $start = $i + 1;
                $tank = 0;
            }
        }
        return $total >= 0 ? $start : -1;
    }
}