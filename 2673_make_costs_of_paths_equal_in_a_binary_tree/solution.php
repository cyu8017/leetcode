<?php
// LeetCode 2673 - Make Costs of Paths Equal in a Binary Tree
// https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/

class Solution {
    function minIncrements($n, $cost) {
        $ans = 0;
        for ($i = intdiv($n, 2) - 1; $i >= 0; $i--) {
            $l = 2 * $i + 1;
            $r = 2 * $i + 2;
            $ans += abs($cost[$l] - $cost[$r]);
            $cost[$i] += max($cost[$l], $cost[$r]);
        }
        return $ans;
    }
}
