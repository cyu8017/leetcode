<?php
// LeetCode 0778 - Swim in Rising Water
// https://leetcode.com/problems/swim-in-rising-water/

class Solution {
    function swimInWater($grid) {
        $n = count($grid);
        $heap = [[$grid[0][0], 0, 0]];
        $seen = array_fill(0, $n, array_fill(0, $n, false));
        $seen[0][0] = true;
        $dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]];
        while (count($heap) > 0) {
            usort($heap, function ($a, $b) { return $a[0] - $b[0]; });
            $item = array_shift($heap);
            $time = $item[0];
            $r = $item[1];
            $c = $item[2];
            if ($r === $n - 1 && $c === $n - 1) return $time;
            foreach ($dirs as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                if ($nr >= 0 && $nr < $n && $nc >= 0 && $nc < $n && !$seen[$nr][$nc]) {
                    $seen[$nr][$nc] = true;
                    $nt = max($time, $grid[$nr][$nc]);
                    $heap[] = [$nt, $nr, $nc];
                }
            }
        }
        return -1;
    }
}
