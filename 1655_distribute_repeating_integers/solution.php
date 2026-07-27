<?php
// LeetCode 1655 - Distribute Repeating Integers
// https://leetcode.com/problems/distribute-repeating-integers/

class Solution {
    function canDistribute($nums, $quantity) {
        $freq = [];
        foreach ($nums as $x) {
            $freq[$x] = ($freq[$x] ?? 0) + 1;
        }
        $cnt = array_values($freq);
        rsort($quantity);
        $m = count($quantity);
        $sums = array_fill(0, 1 << $m, 0);
        for ($mask = 1; $mask < (1 << $m); $mask++) {
            $bit = $mask & -$mask;
            $sums[$mask] = $sums[$mask ^ $bit] + $quantity[(int)log($bit, 2)];
        }
        $dp = [0 => true];
        foreach ($cnt as $c) {
            $nxt = $dp;
            foreach (array_keys($dp) as $mask) {
                $left = ((1 << $m) - 1) ^ $mask;
                $sub = $left;
                while ($sub > 0) {
                    if ($sums[$sub] <= $c) {
                        $nxt[$mask | $sub] = true;
                    }
                    $sub = ($sub - 1) & $left;
                }
            }
            $dp = $nxt;
        }
        return isset($dp[(1 << $m) - 1]);
    }
}
