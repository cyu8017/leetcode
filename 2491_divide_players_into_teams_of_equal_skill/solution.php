<?php
// LeetCode 2491 - Divide Players Into Teams of Equal Skill
// https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution {
    function dividePlayers($skill) {
        sort($skill);
        $n = count($skill);
        $target = $skill[0] + $skill[$n - 1];
        $chem = 0;
        for ($i = 0; $i < intdiv($n, 2); $i++) {
            if ($skill[$i] + $skill[$n - 1 - $i] !== $target) return -1;
            $chem += $skill[$i] * $skill[$n - 1 - $i];
        }
        return $chem;
    }
}
