<?php
// LeetCode 0818 - Race Car
// https://leetcode.com/problems/race-car/

class Solution {
    /**
     * @param Integer $target
     * @return Integer
     */
    function racecar($target) {
        $key = function($pos, $speed) {
            return ($pos * 1048576) ^ ($speed & 0xfffff);
        };
        $queue = [[0, 1, 0]];
        $seen = [$key(0, 1) => true];
        $qi = 0;
        while ($qi < count($queue)) {
            $pos = $queue[$qi][0];
            $speed = $queue[$qi][1];
            $steps = $queue[$qi][2];
            $qi++;
            if ($pos === $target) return $steps;
            $nxtPos = $pos + $speed;
            $nxtSpeed = $speed * 2;
            $k1 = $key($nxtPos, $nxtSpeed);
            if (!isset($seen[$k1]) && abs($nxtPos) < $target * 2) {
                $seen[$k1] = true;
                $queue[] = [$nxtPos, $nxtSpeed, $steps + 1];
            }
            $revSpeed = $speed > 0 ? -1 : 1;
            $k2 = $key($pos, $revSpeed);
            if (!isset($seen[$k2])) {
                $seen[$k2] = true;
                $queue[] = [$pos, $revSpeed, $steps + 1];
            }
        }
        return -1;
    }
}
