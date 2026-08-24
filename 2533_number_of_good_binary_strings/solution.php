<?php
// LeetCode 2533 - Number of Good Binary Strings
// https://leetcode.com/problems/number-of-good-binary-strings/

class Solution {
    function goodBinaryStrings($minLength, $maxLength, $oneGroup, $zeroGroup) {
        $MOD = 1000000007;
        $dp = array_fill(0, $maxLength + 1, 0);
        $dp[0] = 1;
        for ($i = 0; $i <= $maxLength; $i++) {
            if ($dp[$i] === 0) continue;
            if ($i + $oneGroup <= $maxLength) $dp[$i + $oneGroup] = ($dp[$i + $oneGroup] + $dp[$i]) % $MOD;
            if ($i + $zeroGroup <= $maxLength) $dp[$i + $zeroGroup] = ($dp[$i + $zeroGroup] + $dp[$i]) % $MOD;
        }
        $ans = 0;
        for ($i = $minLength; $i <= $maxLength; $i++) $ans = ($ans + $dp[$i]) % $MOD;
        return $ans;
    }
}
