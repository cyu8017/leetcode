<?php
// LeetCode 1134 - Armstrong Number
// https://leetcode.com/problems/armstrong-number/

class Solution {
    /**
     * @param Integer $n
     * @return Boolean
     */
    function isArmstrong($n) {
        $s = (string)$n;
        $k = strlen($s);
        $sum = 0;
        foreach (str_split($s) as $ch) {
            $sum += ((int)$ch) ** $k;
        }
        return $sum === $n;
    }
}
