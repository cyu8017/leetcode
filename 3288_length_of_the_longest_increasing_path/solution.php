<?php
// LeetCode 3288 - Length of the Longest Increasing Path
// https://leetcode.com/problems/length-of-the-longest-increasing-path/

class Solution {
    function lis($a) {
        $tails = [];
        foreach ($a as $x) {
            $lo = 0;
            $hi = count($tails);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($tails[$mid] < $x) $lo = $mid + 1;
                else $hi = $mid;
            }
            if ($lo === count($tails)) $tails[] = $x;
            else $tails[$lo] = $x;
        }
        return count($tails);
    }

    function maxPathLength($coordinates, $k) {
        $n = count($coordinates);
        $arr = [];
        for ($i = 0; $i < $n; $i++) $arr[] = [$coordinates[$i][0], $coordinates[$i][1], $i];
        usort($arr, function($a, $b) {
            if ($a[0] === $b[0]) return $b[1] <=> $a[1];
            return $a[0] <=> $b[0];
        });
        $kx = $coordinates[$k][0];
        $ky = $coordinates[$k][1];
        $left = [];
        $right = [];
        foreach ($arr as $p) {
            if ($p[0] < $kx && $p[1] < $ky) $left[] = $p[1];
            if ($p[0] > $kx && $p[1] > $ky) $right[] = $p[1];
        }
        return $this->lis($left) + 1 + $this->lis($right);
    }
}
