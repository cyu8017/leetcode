<?php
// LeetCode 2576 - Find the Maximum Number of Marked Indices
// https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/

class Solution {
    function maxNumOfMarkedIndices($nums) {
        sort($nums);
        $n = count($nums);
        $i = 0;
        $ans = 0;
        for ($j = intdiv($n + 1, 2); $j < $n; $j++) {
            if (2 * $nums[$i] <= $nums[$j]) {
                $ans += 2;
                $i++;
            }
        }
        return $ans;
    }
}
