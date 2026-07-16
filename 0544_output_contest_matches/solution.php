<?php
// LeetCode 0544 - Output Contest Matches
// https://leetcode.com/problems/output-contest-matches/

class Solution {
    /**
     * @param Integer $n
     * @return String
     */
    function findContestMatch($n) {
        return $this->find_contest_match($n);
    }

    /**
     * @param Integer $n
     * @return String
     */
    function find_contest_match($n) {
        $teams = [];
        for ($i = 1; $i <= $n; $i++) {
            $teams[] = (string)$i;
        }
        while (count($teams) > 1) {
            $nextRound = [];
            $half = intdiv(count($teams), 2);
            for ($i = 0; $i < $half; $i++) {
                $nextRound[] = '(' . $teams[$i] . ',' . $teams[count($teams) - 1 - $i] . ')';
            }
            $teams = $nextRound;
        }
        return $teams[0];
    }
}
