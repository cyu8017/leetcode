<?php
// LeetCode 0724 - Find Pivot Index
// https://leetcode.com/problems/find-pivot-index/

class Solution {
    function pivotIndex($nums) {
        $total = 0;
        foreach ($nums as $x) $total += $x;
        $left = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($left === $total - $left - $nums[$i]) return $i;
            $left += $nums[$i];
        }
        return -1;
    }
}
