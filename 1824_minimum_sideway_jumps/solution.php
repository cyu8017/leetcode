<?php
// LeetCode 1824 - Minimum Sideway Jumps
// https://leetcode.com/problems/minimum-sideway-jumps/

class Solution {
    /**
     * @param Integer[] $obstacles
     * @return Integer
     */
    function minSideJumps($obstacles) {
        $inf = PHP_INT_MAX / 2;
        $dp = [1, 0, 1];

        foreach ($obstacles as $obs) {
            $blocked = [
                $obs === 1,
                $obs === 2,
                $obs === 3,
            ];
            $ndp = [$inf, $inf, $inf];
            for ($lane = 0; $lane < 3; $lane++) {
                if ($blocked[$lane]) {
                    continue;
                }
                for ($other = 0; $other < 3; $other++) {
                    if ($blocked[$other] || $dp[$other] === $inf) {
                        continue;
                    }
                    $ndp[$lane] = min($ndp[$lane], $dp[$other] + ($lane !== $other ? 1 : 0));
                }
            }
            $dp = $ndp;
        }

        return min($dp);
    }
}
