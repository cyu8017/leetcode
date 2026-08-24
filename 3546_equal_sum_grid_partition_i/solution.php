<?php
// LeetCode 3546 - Equal Sum Grid Partition I
// https://leetcode.com/problems/equal-sum-grid-partition-i/

class Solution {
    function canPartitionGrid($grid) {
        $s = 0;
        foreach ($grid as $row) foreach ($row as $x) $s += $x;
        if ($s % 2 !== 0) return false;
        $m = count($grid);
        $n = count($grid[0]);
        $pre = 0;
        for ($i = 0; $i < $m; $i++) {
            foreach ($grid[$i] as $x) $pre += $x;
            if ($pre * 2 === $s && $i + 1 < $m) return true;
        }
        $pre = 0;
        for ($j = 0; $j < $n; $j++) {
            for ($i = 0; $i < $m; $i++) $pre += $grid[$i][$j];
            if ($pre * 2 === $s && $j + 1 < $n) return true;
        }
        return false;
    }
}
