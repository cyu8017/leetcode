<?php
// LeetCode 1057 - Campus Bikes
// https://leetcode.com/problems/campus-bikes/

class Solution {
    /**
     * @param Integer[][] $workers
     * @param Integer[][] $bikes
     * @return Integer[]
     */
    function assignBikes($workers, $bikes) {
        $triples = [];
        foreach ($workers as $w => $worker) {
            foreach ($bikes as $b => $bike) {
                $dist = abs($worker[0] - $bike[0]) + abs($worker[1] - $bike[1]);
                $triples[] = [$dist, $w, $b];
            }
        }
        usort($triples, function ($a, $b) {
            if ($a[0] !== $b[0]) {
                return $a[0] <=> $b[0];
            }
            if ($a[1] !== $b[1]) {
                return $a[1] <=> $b[1];
            }
            return $a[2] <=> $b[2];
        });
        $ans = array_fill(0, count($workers), -1);
        $usedBikes = [];
        $assigned = 0;
        foreach ($triples as [$dist, $w, $b]) {
            if ($ans[$w] === -1 && !isset($usedBikes[$b])) {
                $ans[$w] = $b;
                $usedBikes[$b] = true;
                $assigned++;
                if ($assigned === count($workers)) {
                    break;
                }
            }
        }
        return $ans;
    }
}
