<?php
// LeetCode 3513 - Number of Unique XOR Triplets I
// https://leetcode.com/problems/number-of-unique-xor-triplets-i/

class Solution {
    function uniqueXorTriplets($nums) {
        $n = count($nums);
        if ($n <= 2) return $n;
        $x = $n;
        $len = 0;
        while ($x !== 0) { $len++; $x >>= 1; }
        return 1 << $len;
    }
}
