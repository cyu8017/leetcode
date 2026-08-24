<?php
// LeetCode 3847 - Find the Score Difference in a Game
// https://leetcode.com/problems/find-the-score-difference-in-a-game/

class Solution {
    function scoreDifference($nums) {
        $ans = 0;
        $k = 1;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] % 2 !== 0) $k = -$k;
            if ($i % 6 === 5) $k = -$k;
            $ans += $k * $nums[$i];
        }
        return $ans;
    }
}
