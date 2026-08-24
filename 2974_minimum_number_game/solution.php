<?php
// LeetCode 2974 - Minimum Number Game
// https://leetcode.com/problems/minimum-number-game/

class Solution {
    function numberGame($nums) {
        sort($nums);
        for ($i = 0; $i + 1 < count($nums); $i += 2) {
            $t = $nums[$i];
            $nums[$i] = $nums[$i + 1];
            $nums[$i + 1] = $t;
        }
        return $nums;
    }
}
