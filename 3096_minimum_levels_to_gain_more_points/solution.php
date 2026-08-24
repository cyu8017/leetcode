<?php
// LeetCode 3096 - Minimum Levels to Gain More Points
// https://leetcode.com/problems/minimum-levels-to-gain-more-points/

class Solution {
    function minimumLevels($possible) {
        $s = 0;
        foreach ($possible as $x) $s += ($x === 0 ? -1 : $x);
        $t = 0;
        $n = count($possible);
        for ($i = 0; $i + 1 < $n; $i++) {
            $x = $possible[$i] === 0 ? -1 : $possible[$i];
            $t += $x;
            if ($t > $s - $t) return $i + 1;
        }
        return -1;
    }
}
