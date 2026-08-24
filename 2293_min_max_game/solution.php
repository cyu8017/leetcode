<?php
// LeetCode 2293 - Min Max Game
// https://leetcode.com/problems/min-max-game/

class Solution {
    function minMaxGame($nums) {
        while (count($nums) > 1) {
            $next = [];
            $m = count($nums) >> 1;
            for ($i = 0; $i < $m; $i++) {
                if ($i % 2 === 0) $next[] = min($nums[2 * $i], $nums[2 * $i + 1]);
                else $next[] = max($nums[2 * $i], $nums[2 * $i + 1]);
            }
            $nums = $next;
        }
        return $nums[0];
    }
}
