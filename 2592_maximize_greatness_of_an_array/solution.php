<?php
// LeetCode 2592 - Maximize Greatness of an Array
// https://leetcode.com/problems/maximize-greatness-of-an-array/

class Solution {
    function maximizeGreatness($nums) {
        sort($nums);
        $i = 0;
        foreach ($nums as $x) {
            if ($x > $nums[$i]) $i++;
        }
        return $i;
    }
}
