<?php
// LeetCode 1817 - Finding the Users Active Minutes
// https://leetcode.com/problems/finding-the-users-active-minutes/

class Solution {
    /**
     * @param Integer[][] $logs
     * @param Integer $k
     * @return Integer[]
     */
    function findingUsersActiveMinutes($logs, $k) {
        $userMinutes = [];
        foreach ($logs as $log) {
            $userMinutes[$log[0]][$log[1]] = true;
        }

        $answer = array_fill(0, $k, 0);
        foreach ($userMinutes as $minutes) {
            $uam = count($minutes);
            if ($uam <= $k) {
                $answer[$uam - 1]++;
            }
        }
        return $answer;
    }
}
