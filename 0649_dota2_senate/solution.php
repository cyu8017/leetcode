<?php
// LeetCode 0649 - Dota2 Senate
// https://leetcode.com/problems/dota2-senate/

class Solution {
    function predictPartyVictory($senate) {
        $radiant = [];
        $dire = [];
        $n = strlen($senate);
        for ($i = 0; $i < $n; ++$i) {
            if ($senate[$i] === "R") $radiant[] = $i;
            else $dire[] = $i;
        }
        while ($radiant && $dire) {
            $r = array_shift($radiant);
            $d = array_shift($dire);
            if ($r < $d) $radiant[] = $r + $n;
            else $dire[] = $d + $n;
        }
        return $radiant ? "Radiant" : "Dire";
    }
}
