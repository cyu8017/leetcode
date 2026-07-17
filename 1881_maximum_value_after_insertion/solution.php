<?php
// LeetCode 1881 - Maximum Value after Insertion
// https://leetcode.com/problems/maximum-value-after-insertion/

class Solution {
    /**
     * @param String $n
     * @param Integer $x
     * @return String
     */
    function maxValue($n, $x) {
        $neg = $n[0] === '-';
        $start = $neg ? 1 : 0;
        $len = strlen($n);
        for ($i = $start; $i < $len; $i++) {
            $d = (int)$n[$i];
            if ($neg) {
                if ($d > $x) {
                    return substr($n, 0, $i) . (string)$x . substr($n, $i);
                }
            } elseif ($d < $x) {
                return substr($n, 0, $i) . (string)$x . substr($n, $i);
            }
        }
        return $n . (string)$x;
    }
}
