<?php
// LeetCode 2997 - Minimum Number of Operations to Make Array XOR Equal to K
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution {
    function minOperations($nums, $k) {
        $xorr = 0;
        foreach ($nums as $v) $xorr ^= $v;
        $diff = $xorr ^ $k;
        $ans = 0;
        while ($diff > 0) {
            $ans += $diff & 1;
            $diff >>= 1;
        }
        return $ans;
    }
}
