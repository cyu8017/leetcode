<?php
// LeetCode 2015 - Average Height of Buildings in Each Segment
// https://leetcode.com/problems/average-height-of-buildings-in-each-segment/

class Solution {
    /**
     * @param Integer[][] $buildings
     * @return Integer[][]
     */
    function averageHeightOfBuildings($buildings) {
        $events = [];
        foreach ($buildings as $b) {
            $events[] = [$b[0], 1, $b[2]];
            $events[] = [$b[1], -1, $b[2]];
        }
        usort($events, function ($a, $b) {
            if ($a[0] !== $b[0]) return $a[0] <=> $b[0];
            return $a[1] <=> $b[1];
        });
        $ans = [];
        $count = 0;
        $sum = 0;
        $prev = $events[0][0];
        foreach ($events as $e) {
            if ($e[0] !== $prev && $count > 0) {
                $avg = intdiv($sum, $count);
                $last = count($ans) - 1;
                if ($last >= 0 && $ans[$last][1] === $prev && $ans[$last][2] === $avg)
                    $ans[$last][1] = $e[0];
                else $ans[] = [$prev, $e[0], $avg];
            }
            $count += $e[1];
            $sum += $e[1] * $e[2];
            $prev = $e[0];
        }
        return $ans;
    }
}
