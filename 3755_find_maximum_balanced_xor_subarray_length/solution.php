<?php
// LeetCode 3755 - Find Maximum Balanced XOR Subarray Length
// https://leetcode.com/problems/find-maximum-balanced-xor-subarray-length/

class Solution {
    function maxBalancedSubarray($nums) {
        $d = [];
        $a = 0;
        $b = count($nums);
        $ans = 0;
        $d[$b] = -1;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $a ^= $nums[$i];
            if ($nums[$i] % 2 === 0) $b++;
            else $b--;
            $key = ($a << 32) | ($b & 0xffffffff);
            if (isset($d[$key])) $ans = max($ans, $i - $d[$key]);
            else $d[$key] = $i;
        }
        return $ans;
    }
}
