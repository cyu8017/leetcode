<?php
// LeetCode 1238 - Circular Permutation in Binary Representation
// https://leetcode.com/problems/circular-permutation-in-binary-representation/

class Solution {
    /**
     * @param Integer $n
     * @param Integer $start
     * @return Integer[]
     */
    function circularPermutation($n, $start) {
        $ans = [];
        $limit = 1 << $n;
        for ($i = 0; $i < $limit; $i++) {
            $ans[] = $start ^ $i ^ ($i >> 1);
        }
        return $ans;
    }
}
