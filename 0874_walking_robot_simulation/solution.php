<?php
// LeetCode 0874 - Walking Robot Simulation
// https://leetcode.com/problems/walking-robot-simulation/

class Solution {
    /**
     * @param Integer[] $commands
     * @param Integer[][] $obstacles
     * @return Integer
     */
    function robotSim($commands, $obstacles) {
        $encode = function($x, $y) {
            return (($x + 30000) << 20) | ($y + 30000);
        };
        $blocked = [];
        foreach ($obstacles as $o) $blocked[$encode($o[0], $o[1])] = true;
        $dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
        $x = 0;
        $y = 0;
        $d = 0;
        $best = 0;
        foreach ($commands as $cmd) {
            if ($cmd === -1) $d = ($d + 1) % 4;
            elseif ($cmd === -2) $d = ($d + 3) % 4;
            else {
                $dx = $dirs[$d][0];
                $dy = $dirs[$d][1];
                for ($step = 0; $step < $cmd; $step++) {
                    $nx = $x + $dx;
                    $ny = $y + $dy;
                    if (isset($blocked[$encode($nx, $ny)])) break;
                    $x = $nx;
                    $y = $ny;
                }
                $best = max($best, $x * $x + $y * $y);
            }
        }
        return $best;
    }
}
