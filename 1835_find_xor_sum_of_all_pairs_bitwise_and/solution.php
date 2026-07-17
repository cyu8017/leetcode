<?php
// LeetCode 1835 - Find XOR Sum of All Pairs Bitwise AND
// https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/

class Solution {
    /**
     * @param Integer[] $arr1
     * @param Integer[] $arr2
     * @return Integer
     */
    function getXORSum($arr1, $arr2) {
        $xor1 = 0;
        foreach ($arr1 as $value) {
            $xor1 ^= $value;
        }
        $xor2 = 0;
        foreach ($arr2 as $value) {
            $xor2 ^= $value;
        }
        return $xor1 & $xor2;
    }
}
