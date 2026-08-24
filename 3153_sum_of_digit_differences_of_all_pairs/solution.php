<?php
// LeetCode 3153 - Sum of Digit Differences of All Pairs
// https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/

class Solution {
    function sumDigitDifferences($nums) {
        $n = count($nums);
        $m = (int)floor(log10($nums[0])) + 1;
        $ans = 0;
        $vals = $nums;
        for ($k = 0; $k < $m; $k++) {
            $cnt = array_fill(0, 10, 0);
            for ($i = 0; $i < $n; $i++) {
                $cnt[$vals[$i] % 10]++;
                $vals[$i] = intdiv($vals[$i], 10);
            }
            foreach ($cnt as $v) $ans += $v * ($n - $v);
        }
        return intdiv($ans, 2);
    }
}
