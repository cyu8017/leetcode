<?php
// LeetCode 1282 - Group the People Given the Group Size They Belong To
// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

class Solution {
    /**
     * @param Integer[] $groupSizes
     * @return Integer[][]
     */
    function groupThePeople($groupSizes) {
        $pending = [];
        $answer = [];
        foreach ($groupSizes as $person => $size) {
            $pending[$size][] = $person;
            if (count($pending[$size]) === $size) {
                $answer[] = $pending[$size];
                $pending[$size] = [];
            }
        }
        usort($answer, function ($a, $b) {
            $cmp = count($a) <=> count($b);
            return $cmp !== 0 ? $cmp : $a <=> $b;
        });
        return $answer;
    }
}
