<?php
// LeetCode 3661 - Maximum Walls Destroyed by Robots
// https://leetcode.com/problems/maximum-walls-destroyed-by-robots/

class Solution {
    function maxWalls($robots, $distance, $walls) {
        $n = count($robots);
        $arr = [];
        for ($i = 0; $i < $n; $i++) $arr[] = [$robots[$i], $distance[$i]];
        usort($arr, function($a, $b) { return $a[0] <=> $b[0]; });
        sort($walls);
        $lowerBound = function($a, $target) {
            $lo = 0;
            $hi = count($a);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($a[$mid] < $target) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo;
        };
        $memo = [];
        $dfs = function($i, $j) use (&$dfs, &$memo, $arr, $walls, $lowerBound) {
            if ($i < 0) return 0;
            $key = ($i << 1) | $j;
            if (isset($memo[$key])) return $memo[$key];
            $left = $arr[$i][0] - $arr[$i][1];
            if ($i > 0) $left = max($left, $arr[$i - 1][0] + 1);
            $l = $lowerBound($walls, $left);
            $r = $lowerBound($walls, $arr[$i][0] + 1);
            $ans = $dfs($i - 1, 0) + ($r - $l);
            $right = $arr[$i][0] + $arr[$i][1];
            if ($i + 1 < count($arr)) {
                if ($j === 0) $right = min($right, $arr[$i + 1][0] - $arr[$i + 1][1] - 1);
                else $right = min($right, $arr[$i + 1][0] - 1);
            }
            $l = $lowerBound($walls, $arr[$i][0]);
            $r = $lowerBound($walls, $right + 1);
            $ans = max($ans, $dfs($i - 1, 1) + ($r - $l));
            $memo[$key] = $ans;
            return $ans;
        };
        return $dfs($n - 1, 1);
    }
}
