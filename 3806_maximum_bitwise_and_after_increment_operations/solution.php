<?php
// LeetCode 3806 - Maximum Bitwise AND After Increment Operations
// https://leetcode.com/problems/maximum-bitwise-and-after-increment-operations/

class Solution {
    function maximumAND($nums, $k, $m) {
        $BitLen = function($x) {
            if ($x === 0) return 0;
            $n = 0;
            while ($x > 0) { $n++; $x >>= 1; }
            return $n;
        };
        $mxVal = $nums[0];
        foreach ($nums as $v) if ($v > $mxVal) $mxVal = $v;
        $mxVal += $k;
        $mx = $BitLen($mxVal);
        $ans = 0;
        $cost = array_fill(0, count($nums), 0);
        for ($bit = $mx - 1; $bit >= 0; $bit--) {
            $target = $ans | (1 << $bit);
            for ($i = 0; $i < count($nums); $i++) {
                $x = $nums[$i];
                $j = $BitLen($target & ~$x);
                $mask = (1 << $j) - 1;
                $cost[$i] = ($target & $mask) - ($x & $mask);
            }
            sort($cost);
            $sum = 0;
            for ($i = 0; $i < $m; $i++) $sum += $cost[$i];
            if ($sum <= $k) $ans = $target;
        }
        return $ans;
    }
}
