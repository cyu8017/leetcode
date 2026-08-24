<?php
// LeetCode 3190 - Find Minimum Operations to Make All Elements Divisible by Three
// https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

class Solution {
    function minimumOperations($nums) {
        $ans = 0;
        foreach ($nums as $x) if ($x % 3 !== 0) $ans++;
        return $ans;
    }
}
