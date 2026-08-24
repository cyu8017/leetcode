<?php
// LeetCode 3207 - Maximum Points After Enemy Battles
// https://leetcode.com/problems/maximum-points-after-enemy-battles/

class Solution {
    function maximumPoints($enemyEnergies, $currentEnergy) {
        sort($enemyEnergies);
        if ($currentEnergy < $enemyEnergies[0]) return 0;
        $ans = 0;
        for ($i = count($enemyEnergies) - 1; $i >= 0; $i--) {
            $ans += intdiv($currentEnergy, $enemyEnergies[0]);
            $currentEnergy %= $enemyEnergies[0];
            $currentEnergy += $enemyEnergies[$i];
        }
        return $ans;
    }
}
