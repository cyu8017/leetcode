<?php
// LeetCode 2902 - Count of Sub-Multisets With Bounded Sum
// https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/

class Solution {
    function countSubMultisets($nums, $l, $r) {
        $mod = 1000000007;
        $freq = [];
        $total = 0;
        foreach ($nums as $v) {
            if (!isset($freq[$v])) $freq[$v] = 0;
            $freq[$v]++;
            $total += $v;
        }
        if ($total < $l) return 0;
        if ($r > $total) $r = $total;
        $dp = array_fill(0, $r + 1, 0);
        $dp[0] = 1;
        $zeros = $freq[0] ?? 0;
        unset($freq[0]);
        foreach ($freq as $v => $c) {
            $ndp = array_fill(0, $r + 1, 0);
            for ($sum = 0; $sum <= $r; $sum++) {
                if ($dp[$sum] === 0) continue;
                for ($k = 0; $k <= $c && $sum + $k * $v <= $r; $k++)
                    $ndp[$sum + $k * $v] = ($ndp[$sum + $k * $v] + $dp[$sum]) % $mod;
            }
            $dp = $ndp;
        }
        $ans = 0;
        for ($s = $l; $s <= $r; $s++) $ans = ($ans + $dp[$s]) % $mod;
        $ans = ($ans * ($zeros + 1)) % $mod;
        return (int)$ans;
    }
}
