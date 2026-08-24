<?php
// LeetCode 0860 - Lemonade Change
// https://leetcode.com/problems/lemonade-change/

class Solution {
    /**
     * @param Integer[] $bills
     * @return Boolean
     */
    function lemonadeChange($bills) {
        $fives = 0;
        $tens = 0;
        foreach ($bills as $bill) {
            if ($bill === 5) $fives++;
            elseif ($bill === 10) {
                if ($fives === 0) return false;
                $fives--;
                $tens++;
            } else {
                if ($tens > 0 && $fives > 0) { $tens--; $fives--; }
                elseif ($fives >= 3) $fives -= 3;
                else return false;
            }
        }
        return true;
    }
}
