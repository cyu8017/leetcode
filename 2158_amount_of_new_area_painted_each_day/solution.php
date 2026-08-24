<?php
// LeetCode 2158 - Amount of New Area Painted Each Day
// https://leetcode.com/problems/amount-of-new-area-painted-each-day/

class Solution {
    /**
     * @param Integer[][] $paint
     * @return Integer[]
     */
    function amountPainted($paint) {
        $ans = array_fill(0, count($paint), 0);
        $line = array_fill(0, 50001, 0);
        for ($i = 0; $i < count($paint); $i++) {
            $start = $paint[$i][0];
            $end = $paint[$i][1];
            $j = $start;
            while ($j < $end) {
                if ($line[$j] === 0) {
                    $ans[$i]++;
                    $line[$j] = $end;
                    $j++;
                } else {
                    $next = $line[$j];
                    $line[$j] = max($end, $next);
                    $j = $next;
                }
            }
        }
        return $ans;
    }
}
