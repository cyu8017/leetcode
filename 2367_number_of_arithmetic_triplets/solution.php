<?php
// LeetCode 2367 - Number of Arithmetic Triplets
// https://leetcode.com/problems/number-of-arithmetic-triplets/

class Solution {
    function arithmeticTriplets($nums, $diff) {
        $seen = [];
        foreach ($nums as $x) $seen[$x] = true;
        $ans = 0;
        foreach ($nums as $x) {
            if (isset($seen[$x + $diff]) && isset($seen[$x + 2 * $diff])) $ans++;
        }
        return $ans;
    }
}
