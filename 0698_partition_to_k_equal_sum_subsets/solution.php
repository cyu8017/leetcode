<?php
// LeetCode 0698 - Partition to K Equal Sum Subsets
// https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution {
    function canPartitionKSubsets($nums, $k) {
        $total = 0;
        foreach ($nums as $x) $total += $x;
        if ($total % $k !== 0) return false;
        $target = intdiv($total, $k);
        $arr = $nums;
        rsort($arr);
        if ($arr[0] > $target) return false;
        $buckets = array_fill(0, $k, 0);
        $dfs = function ($index) use (&$dfs, &$arr, &$buckets, $target) {
            if ($index === count($arr)) return true;
            for ($i = 0; $i < count($buckets); $i++) {
                if ($buckets[$i] + $arr[$index] > $target) continue;
                $buckets[$i] += $arr[$index];
                if ($dfs($index + 1)) return true;
                $buckets[$i] -= $arr[$index];
                if ($buckets[$i] === 0) break;
            }
            return false;
        };
        return $dfs(0);
    }
}
