<?php
// LeetCode 3046 - Split the Array
// https://leetcode.com/problems/split-the-array/

class Solution {
    function isPossibleToSplit($nums) {
        $cnt = array_fill(0, 101, 0);
        foreach ($nums as $x) {
            $cnt[$x]++;
            if ($cnt[$x] >= 3) return false;
        }
        return true;
    }
}
