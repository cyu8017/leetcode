<?php
// LeetCode 0887 - Super Egg Drop
// https://leetcode.com/problems/super-egg-drop/

class Solution {
    function superEggDrop($k, $n) {
        $dp = array_fill(0, $k + 1, 0);
        $moves = 0;
        while ($dp[$k] < $n) {
            $moves++;
            for ($eggs = $k; $eggs >= 1; $eggs--) {
                $dp[$eggs] = $dp[$eggs] + $dp[$eggs - 1] + 1;
            }
        }
        return $moves;
    }
}
