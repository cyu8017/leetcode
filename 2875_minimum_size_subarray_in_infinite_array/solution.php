<?php
// LeetCode 2875 - Minimum Size Subarray in Infinite Array
// https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

class Solution {
    function minSizeSubarray($nums, $target) {
        $n = count($nums);
        $total = 0;
        foreach ($nums as $v) $total += $v;
        $INF = 1 << 30;
        $ans = $INF;
        if ($total > 0) {
            $loops = intdiv($target, $total);
            $remain = $target % $total;
            if ($remain === 0) return $loops * $n;
            $arr = array_merge($nums, $nums);
            $left = 0;
            $sum = 0;
            $best = $INF;
            $len = count($arr);
            for ($right = 0; $right < $len; $right++) {
                $sum += $arr[$right];
                while ($sum > $remain && $left <= $right) {
                    $sum -= $arr[$left];
                    $left++;
                }
                if ($sum === $remain && $right - $left + 1 < $best) $best = $right - $left + 1;
            }
            if ($best < $INF) $ans = $loops * $n + $best;
        }
        return $ans === $INF ? -1 : $ans;
    }
}
