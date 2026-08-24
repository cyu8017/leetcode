<?php
// LeetCode 2736 - Maximum Sum Queries
// https://leetcode.com/problems/maximum-sum-queries/

class Solution {
    function maximumSumQueries($nums1, $nums2, $queries) {
        $n = count($nums1);
        $pts = [];
        for ($i = 0; $i < $n; $i++) $pts[] = [$nums1[$i], $nums2[$i], $nums1[$i] + $nums2[$i]];
        usort($pts, function($a, $b) { return $b[0] <=> $a[0]; });
        $qs = [];
        foreach ($queries as $i => $q) $qs[] = [$q[0], $q[1], $i];
        usort($qs, function($a, $b) { return $b[0] <=> $a[0]; });
        $ys = array_merge($nums2, array_map(function($q) { return $q[1]; }, $queries));
        sort($ys);
        $uniq = [];
        foreach ($ys as $y) {
            if (!$uniq || $uniq[count($uniq) - 1] !== $y) $uniq[] = $y;
        }
        $m = count($uniq);
        $bit = array_fill(0, $m + 2, -1);
        $rank = function($y) use ($uniq, $m) {
            $lo = 0;
            $hi = $m;
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($uniq[$mid] < $y) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo + 1;
        };
        $update = function($i, $v) use (&$bit, $m) {
            for (; $i <= $m; $i += $i & -$i) $bit[$i] = max($bit[$i], $v);
        };
        $query = function($i) use (&$bit) {
            $best = -1;
            for (; $i > 0; $i -= $i & -$i) $best = max($best, $bit[$i]);
            return $best;
        };
        $ans = array_fill(0, count($queries), -1);
        $j = 0;
        foreach ($qs as $q) {
            while ($j < $n && $pts[$j][0] >= $q[0]) {
                $update($m - $rank($pts[$j][1]) + 1, $pts[$j][2]);
                $j++;
            }
            $ans[$q[2]] = $query($m - $rank($q[1]) + 1);
        }
        return $ans;
    }
}
