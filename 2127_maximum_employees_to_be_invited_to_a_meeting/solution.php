<?php
// LeetCode 2127 - Maximum Employees to Be Invited to a Meeting
// https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/

class Solution {
    /**
     * @param Integer[] $favorite
     * @return Integer
     */
    function maximumInvitations($favorite) {
        $n = count($favorite);
        $indeg = array_fill(0, $n, 0);
        $depth = array_fill(0, $n, 1);
        foreach ($favorite as $f) $indeg[$f]++;
        $q = [];
        for ($i = 0; $i < $n; $i++) if ($indeg[$i] === 0) $q[] = $i;
        while ($q) {
            $u = array_shift($q);
            $v = $favorite[$u];
            $depth[$v] = max($depth[$v], $depth[$u] + 1);
            if (--$indeg[$v] === 0) $q[] = $v;
        }
        $pairSum = 0;
        $maxCycle = 0;
        $vis = array_fill(0, $n, false);
        for ($i = 0; $i < $n; $i++) {
            if ($indeg[$i] === 0 || $vis[$i]) continue;
            $u = $i;
            $lenCycle = 0;
            while (!$vis[$u]) {
                $vis[$u] = true;
                $u = $favorite[$u];
                $lenCycle++;
            }
            if ($lenCycle === 2) $pairSum += $depth[$i] + $depth[$favorite[$i]];
            else $maxCycle = max($maxCycle, $lenCycle);
        }
        return max($pairSum, $maxCycle);
    }
}
