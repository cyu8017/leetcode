<?php
// LeetCode 3494 - Find the Minimum Amount of Time to Brew Potions
// https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/

class Solution {
    function minTime($skill, $mana) {
        $n = count($skill);
        $m = count($mana);
        $done = array_fill(0, $n, 0);
        for ($j = 0; $j < $m; $j++) {
            $t = 0;
            for ($i = 0; $i < $n; $i++) {
                if ($done[$i] > $t) $t = $done[$i];
                $t += $skill[$i] * $mana[$j];
                $done[$i] = $t;
            }
            for ($i = $n - 2; $i >= 0; $i--)
                $done[$i] = $done[$i + 1] - $skill[$i + 1] * $mana[$j];
        }
        return $done[$n - 1];
    }
}
