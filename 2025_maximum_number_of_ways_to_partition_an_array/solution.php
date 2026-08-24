<?php
// LeetCode 2025 - Maximum Number of Ways to Partition an Array
// https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function waysToPartition($nums, $k) {
        $n = count($nums);
        $pref = array_fill(0, $n, 0);
        $pref[0] = $nums[0];
        for ($i = 1; $i < $n; $i++) $pref[$i] = $pref[$i - 1] + $nums[$i];
        $total = $pref[$n - 1];
        $right = [];
        $left = [];
        for ($i = 0; $i < $n - 1; $i++) $right[$pref[$i]] = ($right[$pref[$i]] ?? 0) + 1;
        $ans = 0;
        if ($total % 2 === 0) $ans = $right[intdiv($total, 2)] ?? 0;
        for ($i = 0; $i < $n; $i++) {
            $diff = $k - $nums[$i];
            $newTotal = $total + $diff;
            $cur = 0;
            if ($newTotal % 2 === 0) {
                $half = intdiv($newTotal, 2);
                $cur = ($left[$half] ?? 0) + ($right[$half - $diff] ?? 0);
            }
            $ans = max($ans, $cur);
            if ($i < $n - 1) {
                $left[$pref[$i]] = ($left[$pref[$i]] ?? 0) + 1;
                $right[$pref[$i]]--;
            }
        }
        return $ans;
    }
}
