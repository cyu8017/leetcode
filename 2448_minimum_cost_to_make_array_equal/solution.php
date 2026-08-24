<?php
// LeetCode 2448 - Minimum Cost to Make Array Equal
// https://leetcode.com/problems/minimum-cost-to-make-array-equal/

class Solution {
    function minCost($nums, $cost) {
        $n = count($nums);
        $idx = range(0, $n - 1);
        usort($idx, function ($a, $b) use ($nums) {
            return $nums[$a] <=> $nums[$b];
        });
        $totalCost = 0;
        foreach ($cost as $c) $totalCost += $c;
        $pref = 0;
        $median = 0;
        foreach ($idx as $i) {
            $pref += $cost[$i];
            if ($pref * 2 >= $totalCost) {
                $median = $nums[$i];
                break;
            }
        }
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $diff = $nums[$i] - $median;
            if ($diff < 0) $diff = -$diff;
            $ans += $diff * $cost[$i];
        }
        return $ans;
    }
}
