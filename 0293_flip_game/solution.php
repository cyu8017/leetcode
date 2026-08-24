<?php
// LeetCode 0293 - Flip Game
// https://leetcode.com/problems/flip-game/

class Solution {
    /**
     * @param String $currentState
     * @return String[]
     */
    function generatePossibleNextMoves($currentState) {
        $result = [];
        $length = strlen($currentState);
        for ($index = 0; $index < $length - 1; $index++) {
            if (substr($currentState, $index, 2) === "++") {
                $result[] = substr($currentState, 0, $index) . "--" . substr($currentState, $index + 2);
            }
        }
        return $result;
    }
}
