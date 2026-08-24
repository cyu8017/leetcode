<?php
// LeetCode 2896 - Apply Operations to Make Two Strings Equal
// https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/

class Solution {
    function minOperations($s1, $s2, $x) {
        $diff = [];
        $n = strlen($s1);
        for ($i = 0; $i < $n; $i++) if ($s1[$i] !== $s2[$i]) $diff[] = $i;
        $m = count($diff);
        if ($m % 2 === 1) return -1;
        if ($m === 0) return 0;
        $dp = array_fill(0, $m + 1, 0);
        $dp[1] = $x;
        for ($i = 1; $i < $m; $i++) {
            $dp[$i + 1] = min($dp[$i] + $x, $dp[$i - 1] + ($diff[$i] - $diff[$i - 1]) * 2);
        }
        return intdiv($dp[$m], 2);
    }
}
