<?php
// LeetCode 2345 - Finding the Number of Visible Mountains
// https://leetcode.com/problems/finding-the-number-of-visible-mountains/

class Solution {
    function visibleMountains($peaks) {
        $arr = [];
        foreach ($peaks as $p) $arr[] = [$p[0] - $p[1], $p[0] + $p[1]];
        usort($arr, function($a, $b) {
            if ($a[0] === $b[0]) return $b[1] - $a[1];
            return $a[0] - $b[0];
        });
        $ans = 0;
        $maxR = PHP_INT_MIN;
        $n = count($arr);
        for ($i = 0; $i < $n; ) {
            $j = $i;
            while ($j < $n && $arr[$j][0] === $arr[$i][0] && $arr[$j][1] === $arr[$i][1]) $j++;
            if ($arr[$i][1] > $maxR) {
                if ($j - $i === 1) $ans++;
                $maxR = $arr[$i][1];
            }
            $i = $j;
        }
        return $ans;
    }
}
