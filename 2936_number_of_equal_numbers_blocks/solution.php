<?php
// LeetCode 2936 - Number of Equal Numbers Blocks
// https://leetcode.com/problems/number-of-equal-numbers-blocks/

class Solution {
    function blockCount($nums) {
        if (!count($nums)) return 0;
        $ans = 1;
        $n = count($nums);
        for ($i = 1; $i < $n; $i++)
            if ($nums[$i] !== $nums[$i - 1]) $ans++;
        return $ans;
    }
}
