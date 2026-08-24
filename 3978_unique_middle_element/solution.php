<?php
// LeetCode 3978 - Unique Middle Element
// https://leetcode.com/problems/unique-middle-element/

class Solution {
    function isMiddleElementUnique($nums) {
        $mid = $nums[intdiv(count($nums), 2)];
        $cnt = 0;
        foreach ($nums as $x) {
            if ($x == $mid) $cnt++;
        }
        return $cnt == 1;
    }
}
