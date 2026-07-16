<?php
// LeetCode 0474 - Ones and Zeroes
// https://leetcode.com/problems/ones-and-zeroes/

class Solution {
    /**
     * @param string[] $strs
     * @param int $m
     * @param int $n
     * @return int
     */
    function findMaxForm($strs, $m, $n) {
        return $this->find_max_form($strs, $m, $n);
    }

    /**
     * @param string[] $strs
     * @param int $m
     * @param int $n
     * @return int
     */
    function find_max_form($strs, $m, $n) {
        $dp = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));
        foreach ($strs as $string) {
            $zeros = substr_count($string, "0");
            $ones = substr_count($string, "1");
            for ($zero = $m; $zero >= $zeros; $zero--) {
                for ($one = $n; $one >= $ones; $one--) {
                    $dp[$zero][$one] = max($dp[$zero][$one], $dp[$zero - $zeros][$one - $ones] + 1);
                }
            }
        }
        return $dp[$m][$n];
    }
}
