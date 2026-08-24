<?php
// LeetCode 0961 - N-Repeated Element in Size 2N Array
// https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

class Solution {
    function repeatedNTimes($nums) {
        $seen = [];
        foreach ($nums as $x) {
            if (isset($seen[$x])) return $x;
            $seen[$x] = true;
        }
        return -1;
    }
}
