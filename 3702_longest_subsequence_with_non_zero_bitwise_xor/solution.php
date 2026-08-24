<?php
// LeetCode 3702 - Longest Subsequence With Non-Zero Bitwise XOR
// https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/

class Solution {
    function longestSubsequence($nums) {
        $xorv = 0;
        $cnt0 = 0;
        foreach ($nums as $x) {
            $xorv ^= $x;
            if ($x === 0) $cnt0++;
        }
        $n = count($nums);
        if ($xorv !== 0) return $n;
        if ($cnt0 === $n) return 0;
        return $n - 1;
    }
}
