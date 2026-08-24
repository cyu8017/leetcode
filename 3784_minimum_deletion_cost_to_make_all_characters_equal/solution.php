<?php
// LeetCode 3784 - Minimum Deletion Cost to Make All Characters Equal
// https://leetcode.com/problems/minimum-deletion-cost-to-make-all-characters-equal/

class Solution {
    function minCost($s, $cost) {
        $tot = 0;
        $g = [];
        for ($i = 0; $i < count($cost); $i++) {
            $tot += $cost[$i];
            if (!isset($g[$s[$i]])) $g[$s[$i]] = 0;
            $g[$s[$i]] += $cost[$i];
        }
        $ans = $tot;
        foreach ($g as $x) $ans = min($ans, $tot - $x);
        return $ans;
    }
}
