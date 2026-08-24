<?php
// LeetCode 2534 - Time Taken to Cross the Door
// https://leetcode.com/problems/time-taken-to-cross-the-door/

class Solution {
    function timeTaken($arrival, $state) {
        $n = count($arrival);
        $ans = array_fill(0, $n, 0);
        $enter = [];
        $exitq = [];
        $i = 0;
        $t = 0;
        $prev = 1;
        while ($i < $n || $enter || $exitq) {
            while ($i < $n && $arrival[$i] <= $t) {
                if ($state[$i] === 0) $enter[] = $i;
                else $exitq[] = $i;
                $i++;
            }
            if (!$enter && !$exitq) {
                if ($i < $n) {
                    $t = $arrival[$i];
                    $prev = 1;
                }
                continue;
            }
            if ($prev === 1) {
                if ($exitq) {
                    $ans[array_shift($exitq)] = $t;
                    $prev = 1;
                } else {
                    $ans[array_shift($enter)] = $t;
                    $prev = 0;
                }
            } else {
                if ($enter) {
                    $ans[array_shift($enter)] = $t;
                    $prev = 0;
                } else {
                    $ans[array_shift($exitq)] = $t;
                    $prev = 1;
                }
            }
            $t++;
        }
        return $ans;
    }
}
