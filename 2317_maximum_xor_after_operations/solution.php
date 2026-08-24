<?php
// LeetCode 2317 - Maximum XOR After Operations
// https://leetcode.com/problems/maximum-xor-after-operations/

class Solution {
    function maximumXOR($nums) {
        $ans = 0;
        foreach ($nums as $x) $ans |= $x;
        return $ans;
    }
}
