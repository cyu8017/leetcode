<?php
// LeetCode 2751 - Robot Collisions
// https://leetcode.com/problems/robot-collisions/

class Solution {
    function survivedRobotsHealths($positions, $healths, $directions) {
        $n = count($positions);
        $idx = range(0, $n - 1);
        usort($idx, function($a, $b) use ($positions) { return $positions[$a] <=> $positions[$b]; });
        $stack = [];
        foreach ($idx as $i) {
            $cur = [$i, $healths[$i], $directions[$i]];
            while ($stack && $stack[count($stack) - 1][2] === 'R' && $cur[2] === 'L') {
                $ti = count($stack) - 1;
                if ($stack[$ti][1] === $cur[1]) {
                    array_pop($stack);
                    $cur[1] = 0;
                    break;
                } else if ($stack[$ti][1] > $cur[1]) {
                    $stack[$ti][1]--;
                    $cur[1] = 0;
                    break;
                } else {
                    $cur[1]--;
                    array_pop($stack);
                }
            }
            if ($cur[1] > 0) $stack[] = $cur;
        }
        $alive = [];
        foreach ($stack as $item) $alive[$item[0]] = $item[1];
        $ans = [];
        for ($i = 0; $i < $n; $i++) if (isset($alive[$i])) $ans[] = $alive[$i];
        return $ans;
    }
}
