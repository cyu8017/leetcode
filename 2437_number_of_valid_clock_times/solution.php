<?php
// LeetCode 2437 - Number of Valid Clock Times
// https://leetcode.com/problems/number-of-valid-clock-times/

class Solution {
    function countTime($time) {
        $ans = 0;
        for ($h = 0; $h < 24; $h++) {
            for ($m = 0; $m < 60; $m++) {
                $h0 = (string)intdiv($h, 10);
                $h1 = (string)($h % 10);
                $m0 = (string)intdiv($m, 10);
                $m1 = (string)($m % 10);
                if ($time[0] !== '?' && $time[0] !== $h0) continue;
                if ($time[1] !== '?' && $time[1] !== $h1) continue;
                if ($time[3] !== '?' && $time[3] !== $m0) continue;
                if ($time[4] !== '?' && $time[4] !== $m1) continue;
                $ans++;
            }
        }
        return $ans;
    }
}
