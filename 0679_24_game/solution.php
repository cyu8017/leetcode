<?php
// LeetCode 0679 - 24 Game
// https://leetcode.com/problems/24-game/

class Solution {
    function judgePoint24($cards) {
        $EPS = 1e-6;
        $dfs = function($nums) use (&$dfs, $EPS) {
            if (count($nums) === 1) return abs($nums[0] - 24) < $EPS;
            for ($i = 0; $i < count($nums); ++$i) {
                for ($j = 0; $j < count($nums); ++$j) {
                    if ($i === $j) continue;
                    $rest = [];
                    for ($k = 0; $k < count($nums); ++$k) {
                        if ($k !== $i && $k !== $j) $rest[] = $nums[$k];
                    }
                    $a = $nums[$i];
                    $b = $nums[$j];
                    $candidates = [$a + $b, $a - $b, $a * $b];
                    if (abs($b) > $EPS) $candidates[] = $a / $b;
                    foreach ($candidates as $value) {
                        $rest[] = $value;
                        if ($dfs($rest)) return true;
                        array_pop($rest);
                    }
                }
            }
            return false;
        };
        $vals = [];
        foreach ($cards as $c) $vals[] = $c * 1.0;
        return $dfs($vals);
    }
}
