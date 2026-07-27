<?php
// LeetCode 1696 - Jump Game VI
// https://leetcode.com/problems/jump-game-vi/

class Solution {
    function maxResult($nums, $k) {
        $q = [[0, $nums[0]]];
        $qi = 0;
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            while ($q[$qi][0] < $i - $k) $qi++;
            $score = $nums[$i] + $q[$qi][1];
            while (count($q) > $qi && $q[count($q) - 1][1] <= $score) array_pop($q);
            $q[] = [$i, $score];
        }
        return $q[count($q) - 1][1];
    }
}
