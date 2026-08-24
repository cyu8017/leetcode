<?php
// LeetCode 3360 - Stone Removal Game
// https://leetcode.com/problems/stone-removal-game/

class Solution {
    function canAliceWin($n) {
        $take = 10;
        $alice = true;
        while ($n >= $take && $take > 0) {
            $n -= $take;
            $take--;
            $alice = !$alice;
        }
        return !$alice;
    }
}
