<?php
// LeetCode 2910 - Minimum Number of Groups to Create a Valid Assignment
// https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/

class Solution {
    function minGroupsForValidAssignment($balls) {
        $freq = [];
        foreach ($balls as $b) {
            if (!isset($freq[$b])) $freq[$b] = 0;
            $freq[$b]++;
        }
        $counts = array_values($freq);
        $minF = min($counts);
        for ($size = $minF; $size >= 1; $size--) {
            $ok = true;
            $groups = 0;
            foreach ($counts as $c) {
                $rem = $c % ($size + 1);
                $g2 = intdiv($c, $size + 1);
                if ($rem === 0) $groups += $g2;
                else if ($size - $rem <= $g2) $groups += $g2 + 1;
                else { $ok = false; break; }
            }
            if ($ok) return $groups;
        }
        return count($balls);
    }
}
