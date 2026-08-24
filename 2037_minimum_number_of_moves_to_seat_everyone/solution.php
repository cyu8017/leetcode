<?php
// LeetCode 2037 - Minimum Number of Moves to Seat Everyone
// https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution {
    /**
     * @param Integer[] $seats
     * @param Integer[] $students
     * @return Integer
     */
    function minMovesToSeat($seats, $students) {
        sort($seats);
        sort($students);
        $ans = 0;
        $n = count($seats);
        for ($i = 0; $i < $n; $i++) $ans += abs($seats[$i] - $students[$i]);
        return $ans;
    }
}
