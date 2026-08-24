<?php
// LeetCode 3542 - Minimum Operations to Convert All Elements to Zero
// https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

class Solution {
    function minOperations($nums) {
        $stk = [];
        $ans = 0;
        foreach ($nums as $x) {
            while (count($stk) > 0 && $stk[count($stk) - 1] > $x) {
                $ans++;
                array_pop($stk);
            }
            if ($x !== 0 && (count($stk) === 0 || $stk[count($stk) - 1] !== $x)) $stk[] = $x;
        }
        $ans += count($stk);
        return $ans;
    }
}
