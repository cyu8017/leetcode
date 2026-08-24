<?php
// LeetCode 2611 - Mice and Cheese
// https://leetcode.com/problems/mice-and-cheese/

class Solution {
    function miceAndCheese($reward1, $reward2, $k) {
        $n = count($reward1);
        $diff = [];
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $ans += $reward2[$i];
            $diff[] = $reward1[$i] - $reward2[$i];
        }
        rsort($diff);
        for ($i = 0; $i < $k; $i++) $ans += $diff[$i];
        return $ans;
    }
}
