<?php
// LeetCode 1829 - Maximum XOR for Each Query
// https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $maximumBit
     * @return Integer[]
     */
    function getMaximumXor($nums, $maximumBit) {
        $limit = (1 << $maximumBit) - 1;
        $current = 0;
        foreach ($nums as $num) {
            $current ^= $num;
        }

        $result = [];
        for ($i = count($nums) - 1; $i >= 0; $i--) {
            $result[] = $current ^ $limit;
            $current ^= $nums[$i];
        }
        return $result;
    }
}
