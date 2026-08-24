<?php
// LeetCode 2527 - Find Xor-Beauty of Array
// https://leetcode.com/problems/find-xor-beauty-of-array/

class Solution {
    function xorBeauty($nums) {
        $ans = 0;
        foreach ($nums as $x) $ans ^= $x;
        return $ans;
    }
}
