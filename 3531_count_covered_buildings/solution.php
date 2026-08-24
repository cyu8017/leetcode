<?php
// LeetCode 3531 - Count Covered Buildings
// https://leetcode.com/problems/count-covered-buildings/

class Solution {
    function countCoveredBuildings($n, $buildings) {
        $g1 = [];
        $g2 = [];
        foreach ($buildings as $b) {
            if (!isset($g1[$b[0]])) $g1[$b[0]] = [];
            if (!isset($g2[$b[1]])) $g2[$b[1]] = [];
            $g1[$b[0]][] = $b[1];
            $g2[$b[1]][] = $b[0];
        }
        foreach ($g1 as &$list) sort($list);
        unset($list);
        foreach ($g2 as &$list) sort($list);
        unset($list);
        $ans = 0;
        foreach ($buildings as $b) {
            $x = $b[0];
            $y = $b[1];
            $l1 = $g1[$x];
            $l2 = $g2[$y];
            if ($l2[0] < $x && $x < $l2[count($l2) - 1] && $l1[0] < $y && $y < $l1[count($l1) - 1]) $ans++;
        }
        return $ans;
    }
}
