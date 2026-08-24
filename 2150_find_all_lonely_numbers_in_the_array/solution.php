<?php
// LeetCode 2150 - Find All Lonely Numbers in the Array
// https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function findLonely($nums) {
        $freq = [];
        foreach ($nums as $x) $freq[$x] = ($freq[$x] ?? 0) + 1;
        $ans = [];
        foreach ($freq as $k => $v) {
            if ($v === 1 && !isset($freq[$k - 1]) && !isset($freq[$k + 1])) $ans[] = $k;
        }
        return $ans;
    }
}
