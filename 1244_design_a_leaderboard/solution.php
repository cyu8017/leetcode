<?php
// LeetCode 1244 - Design A Leaderboard
// https://leetcode.com/problems/design-a-leaderboard/

class Leaderboard {
    private $scores = [];

    function __construct() {}

    /**
     * @param Integer $playerId
     * @param Integer $score
     * @return NULL
     */
    function addScore($playerId, $score) {
        $this->scores[$playerId] = ($this->scores[$playerId] ?? 0) + $score;
    }

    /**
     * @param Integer $K
     * @return Integer
     */
    function top($K) {
        $vals = array_values($this->scores);
        rsort($vals);
        return array_sum(array_slice($vals, 0, $K));
    }

    /**
     * @param Integer $playerId
     * @return NULL
     */
    function reset($playerId) {
        unset($this->scores[$playerId]);
    }
}
