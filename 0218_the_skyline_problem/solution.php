<?php
// LeetCode 0218 - The Skyline Problem
// https://leetcode.com/problems/the-skyline-problem/

class Solution {
    function getSkyline($buildings) {
        $events = [];
        foreach ($buildings as [$left, $right, $height]) {
            $events[] = [$left, -$height, $right];
            $events[] = [$right, 0, 0];
        }
        usort($events, function ($a, $b) {
            if ($a[0] !== $b[0]) {
                return $a[0] <=> $b[0];
            }
            return $a[1] <=> $b[1];
        });

        $result = [];
        $live = [[0, PHP_INT_MAX]];
        foreach ($events as [$x, $negH, $end]) {
            while ($live[0][1] <= $x) {
                array_shift($live);
                if (empty($live)) {
                    $live[] = [0, PHP_INT_MAX];
                }
            }
            if ($negH !== 0) {
                $live[] = [$negH, $end];
                usort($live, function ($a, $b) {
                    return $a[0] <=> $b[0];
                });
            }
            $height = -$live[0][0];
            if (empty($result) || $result[count($result) - 1][1] !== $height) {
                $result[] = [$x, $height];
            }
        }
        return $result;
    }
}
