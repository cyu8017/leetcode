<?php
// LeetCode 3824 - Minimum K to Reduce Array Within Limit
// https://leetcode.com/problems/minimum-k-to-reduce-array-within-limit/

class Solution {
    function check($nums, $k) {
        $t = 0;
        foreach ($nums as $x) $t += intdiv($x + $k - 1, $k);
        return $t <= $k * $k;
    }
    function minimumK($nums) {
        $lo = 1;
        $hi = 100000;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($this->check($nums, $mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
