<?php
// LeetCode 3012 - Minimize Length of Array Using Operations
// https://leetcode.com/problems/minimize-length-of-array-using-operations/

class Solution {
    function minimumArrayLength($nums) {
        $mi = $nums[0];
        foreach ($nums as $x) if ($x < $mi) $mi = $x;
        $cnt = 0;
        foreach ($nums as $x) {
            if ($x % $mi !== 0) return 1;
            if ($x === $mi) $cnt++;
        }
        return intdiv($cnt + 1, 2);
    }
}
