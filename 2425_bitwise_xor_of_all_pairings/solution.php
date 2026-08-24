<?php
// LeetCode 2425 - Bitwise XOR of All Pairings
// https://leetcode.com/problems/bitwise-xor-of-all-pairings/

class Solution {
    function xorAllNums($nums1, $nums2) {
        $ans = 0;
        if (count($nums2) % 2 === 1) foreach ($nums1 as $x) $ans ^= $x;
        if (count($nums1) % 2 === 1) foreach ($nums2 as $x) $ans ^= $x;
        return $ans;
    }
}
