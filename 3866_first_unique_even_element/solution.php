<?php
// LeetCode 3866 - First Unique Even Element
// https://leetcode.com/problems/first-unique-even-element/

class Solution {
    function firstUniqueEven($nums) {
        $cnt = array_fill(0, 101, 0);
        foreach ($nums as $x) $cnt[$x]++;
        foreach ($nums as $x) {
            if ($x % 2 === 0 && $cnt[$x] === 1) return $x;
        }
        return -1;
    }
}
