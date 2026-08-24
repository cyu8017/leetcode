<?php
// LeetCode 0903 - Valid Permutations for DI Sequence
// https://leetcode.com/problems/valid-permutations-for-di-sequence/

class Solution {
    function numPermsDISequence($s) {
        $MOD = 1000000007;
        $n = strlen($s);
        $dp = array_fill(0, $n + 1, 1);
        for ($i = 1; $i <= $n; $i++) {
            $newDp = array_fill(0, $n + 1, 0);
            if ($s[$i - 1] === "I") {
                $postfix = 0;
                for ($j = $n - $i; $j >= 0; $j--) {
                    $postfix = ($postfix + $dp[$j + 1]) % $MOD;
                    $newDp[$j] = $postfix;
                }
            } else {
                $prefix = 0;
                for ($j = 0; $j <= $n - $i; $j++) {
                    $prefix = ($prefix + $dp[$j]) % $MOD;
                    $newDp[$j] = $prefix;
                }
            }
            $dp = $newDp;
        }
        return $dp[0];
    }
}
