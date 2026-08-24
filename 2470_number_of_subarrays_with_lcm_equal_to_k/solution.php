<?php
// LeetCode 2470 - Number of Subarrays With LCM Equal to K
// https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/

class Solution {
    function subarrayLCM($nums, $k) {
        $gcd = function ($a, $b) {
            while ($b !== 0) {
                $t = $a % $b;
                $a = $b;
                $b = $t;
            }
            return $a;
        };
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $cur = 1;
            for ($j = $i; $j < $n; $j++) {
                $cur = intdiv($cur, $gcd($cur, $nums[$j])) * $nums[$j];
                if ($cur > $k) break;
                if ($cur === $k) $ans++;
            }
        }
        return $ans;
    }
}
