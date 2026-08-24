<?php
// LeetCode 3659 - Partition Array Into K-Distinct Groups
// https://leetcode.com/problems/partition-array-into-k-distinct-groups/

class Solution {
    function partitionArray($nums, $k) {
        $n = count($nums);
        if ($n % $k !== 0) return false;
        $m = intdiv($n, $k);
        $mx = 0;
        foreach ($nums as $x) $mx = max($mx, $x);
        $cnt = array_fill(0, $mx + 1, 0);
        foreach ($nums as $x)
            if (++$cnt[$x] > $m) return false;
        return true;
    }
}
