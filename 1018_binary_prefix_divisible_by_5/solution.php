<?php
// LeetCode 1018 - Binary Prefix Divisible By 5
// https://leetcode.com/problems/binary-prefix-divisible-by-5/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Boolean[]
     */
    function prefixesDivBy5($nums) {
        $ans = [];
        $rem = 0;
        foreach ($nums as $bit) {
            $rem = ($rem * 2 + $bit) % 5;
            $ans[] = $rem === 0;
        }
        return $ans;
    }
}
