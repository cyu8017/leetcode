<?php
// LeetCode 0781 - Rabbits in Forest
// https://leetcode.com/problems/rabbits-in-forest/

class Solution {
    /**
     * @param Integer[] $answers
     * @return Integer
     */
    function numRabbits($answers) {
        $counts = [];
        foreach ($answers as $answer) {
            $counts[$answer] = ($counts[$answer] ?? 0) + 1;
        }
        $total = 0;
        foreach ($counts as $key => $value) {
            $group = $key + 1;
            $groups = intdiv($value + $group - 1, $group);
            $total += $groups * $group;
        }
        return $total;
    }
}
