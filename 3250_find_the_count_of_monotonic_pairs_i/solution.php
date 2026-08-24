<?php
// LeetCode 3250 - Find the Count of Monotonic Pairs I
// https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i/

class Solution {
    function countOfPairs($nums) {
        $mod = 1000000007;
        $n = count($nums);
        $dp = array_fill(0, 51, 0);
        for ($a = 0; $a <= $nums[0]; $a++) $dp[$a] = 1;
        for ($i = 1; $i < $n; $i++) {
            $ndp = array_fill(0, 51, 0);
            $pref = array_fill(0, 52, 0);
            for ($a = 0; $a <= 50; $a++) $pref[$a + 1] = ($pref[$a] + $dp[$a]) % $mod;
            for ($a2 = 0; $a2 <= $nums[$i]; $a2++) {
                $b2 = $nums[$i] - $a2;
                $maxA1 = $a2;
                $lim = $nums[$i - 1] - $b2;
                if ($lim < $maxA1) $maxA1 = $lim;
                if ($maxA1 < 0) continue;
                if ($maxA1 > 50) $maxA1 = 50;
                $ndp[$a2] = $pref[$maxA1 + 1];
            }
            $dp = $ndp;
        }
        $ans = 0;
        foreach ($dp as $v) $ans = ($ans + $v) % $mod;
        return $ans;
    }
}
