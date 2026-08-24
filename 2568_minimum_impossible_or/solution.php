<?php
// LeetCode 2568 - Minimum Impossible OR
// https://leetcode.com/problems/minimum-impossible-or/

class Solution {
    function minImpossibleOR($nums) {
        $set = [];
        foreach ($nums as $x) $set[$x] = true;
        $x = 1;
        while (isset($set[$x])) $x <<= 1;
        return $x;
    }
}
