<?php
// LeetCode 0757 - Set Intersection Size At Least Two
// https://leetcode.com/problems/set-intersection-size-at-least-two/

class Solution {
    function intersectionSizeTwo($intervals) {
        usort($intervals, function ($a, $b) {
            return $a[1] !== $b[1] ? $a[1] - $b[1] : $a[0] - $b[0];
        });
        $size = 0;
        $first = -1;
        $second = -1;
        foreach ($intervals as $interval) {
            $left = $interval[0];
            $right = $interval[1];
            if ($left <= $first) continue;
            if ($left <= $second) { $size++; $first = $second; $second = $right; }
            else { $size += 2; $first = $right - 1; $second = $right; }
        }
        return $size;
    }
}
