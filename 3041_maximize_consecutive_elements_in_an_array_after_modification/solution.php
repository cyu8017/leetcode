<?php
// LeetCode 3041 - Maximize Consecutive Elements in an Array After Modification
// https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/

class Solution {
    function maxSelectedElements($nums) {
        sort($nums);
        $dp = [];
        $ans = 0;
        foreach ($nums as $num) {
            $dn = $dp[$num] ?? 0;
            $dnm1 = $dp[$num - 1] ?? 0;
            $dp[$num + 1] = $dn + 1;
            $dp[$num] = $dnm1 + 1;
            $ans = max($ans, max($dp[$num], $dp[$num + 1]));
        }
        return $ans;
    }
}
