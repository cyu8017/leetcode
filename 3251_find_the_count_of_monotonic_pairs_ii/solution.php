<?php
// LeetCode 3251 - Find the Count of Monotonic Pairs II
// https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/

class Solution {
    function countOfPairs($nums) {
        $mod = 1000000007;
        $n = count($nums);
        $maxV = 0;
        foreach ($nums as $v) $maxV = max($maxV, $v);
        $dp = array_fill(0, $maxV + 1, 0);
        for ($a = 0; $a <= $nums[0]; $a++) $dp[$a] = 1;
        for ($i = 1; $i < $n; $i++) {
            $ndp = array_fill(0, $maxV + 1, 0);
            $pref = array_fill(0, $maxV + 2, 0);
            for ($a = 0; $a <= $maxV; $a++) $pref[$a + 1] = ($pref[$a] + $dp[$a]) % $mod;
            for ($a2 = 0; $a2 <= $nums[$i]; $a2++) {
                $b2 = $nums[$i] - $a2;
                $maxA1 = $a2;
                $lim = $nums[$i - 1] - $b2;
                if ($lim < $maxA1) $maxA1 = $lim;
                if ($maxA1 < 0) continue;
                if ($maxA1 > $maxV) $maxA1 = $maxV;
                $ndp[$a2] = $pref[$maxA1 + 1];
            }
            $dp = $ndp;
        }
        $ans = 0;
        foreach ($dp as $v) $ans = ($ans + $v) % $mod;
        return $ans;
    }
}
