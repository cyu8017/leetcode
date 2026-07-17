<?php
// LeetCode 1820 - Maximum Number of Accepted Invitations
// https://leetcode.com/problems/maximum-number-of-accepted-invitations/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maximumInvitations($grid) {
        $boys = count($grid);
        $girls = count($grid[0]);
        $matchGirl = array_fill(0, $girls, -1);

        $dfs = function ($boy, &$seen) use (&$dfs, $grid, $girls, &$matchGirl) {
            for ($girl = 0; $girl < $girls; $girl++) {
                if ($grid[$boy][$girl] && !$seen[$girl]) {
                    $seen[$girl] = true;
                    if ($matchGirl[$girl] === -1 || $dfs($matchGirl[$girl], $seen)) {
                        $matchGirl[$girl] = $boy;
                        return true;
                    }
                }
            }
            return false;
        };

        $ans = 0;
        for ($boy = 0; $boy < $boys; $boy++) {
            $seen = array_fill(0, $girls, false);
            if ($dfs($boy, $seen)) {
                $ans++;
            }
        }
        return $ans;
    }
}
