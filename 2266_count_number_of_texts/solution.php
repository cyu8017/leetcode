<?php
// LeetCode 2266 - Count Number of Texts
// https://leetcode.com/problems/count-number-of-texts/

class Solution {
    function countTexts($pressedKeys) {
        $mod = 1000000007;
        $n = strlen($pressedKeys);
        $dp = array_fill(0, $n + 1, 0);
        $dp[0] = 1;
        for ($i = 1; $i <= $n; $i++) {
            $dp[$i] = $dp[$i - 1];
            $maxPress = ($pressedKeys[$i - 1] === '7' || $pressedKeys[$i - 1] === '9') ? 4 : 3;
            for ($j = 2; $j <= $maxPress && $j <= $i; $j++) {
                if ($pressedKeys[$i - $j] !== $pressedKeys[$i - 1]) break;
                $dp[$i] = ($dp[$i] + $dp[$i - $j]) % $mod;
            }
        }
        return $dp[$n];
    }
}
