<?php
// LeetCode 1796 - Second Largest Digit in a String
// https://leetcode.com/problems/second-largest-digit-in-a-string/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function secondHighest($s) {
        $largest = -1;
        $second = -1;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            if ($ch >= '0' && $ch <= '9') {
                $d = (int)$ch;
                if ($d > $largest) {
                    $second = $largest;
                    $largest = $d;
                } elseif ($d < $largest && $d > $second) {
                    $second = $d;
                }
            }
        }
        return $second;
    }
}
