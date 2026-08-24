<?php
// LeetCode 3994 - Minimum Adjacent Swaps to Partition Array
// https://leetcode.com/problems/minimum-adjacent-swaps-to-partition-array/

class Solution {
    function minAdjacentSwaps($nums, $a, $b) {
        $MOD = 1000000007;
        $result = 0;
        $cnt1 = 0;
        $cnt2 = 0;
        foreach ($nums as $x) {
            if ($x < $a) {
                $result = ($result + $cnt1 + $cnt2) % $MOD;
            } else if ($x <= $b) {
                $cnt1++;
                $result = ($result + $cnt2) % $MOD;
            } else {
                $cnt2++;
            }
        }
        return $result;
    }
}
