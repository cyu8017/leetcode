<?php
// LeetCode 3232 - Find if Digit Game Can Be Won
// https://leetcode.com/problems/find-if-digit-game-can-be-won/

class Solution {
    function canAliceWin($nums) {
        $a = 0;
        $b = 0;
        foreach ($nums as $x) {
            if ($x < 10) $a += $x;
            else $b += $x;
        }
        return $a !== $b;
    }
}
