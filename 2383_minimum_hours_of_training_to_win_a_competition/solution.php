<?php
// LeetCode 2383 - Minimum Hours of Training to Win a Competition
// https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/

class Solution {
    function minNumberOfHours($initialEnergy, $initialExperience, $energy, $experience) {
        $ans = 0;
        $en = $initialEnergy;
        $ex = $initialExperience;
        $n = count($energy);
        for ($i = 0; $i < $n; $i++) {
            if ($en <= $energy[$i]) {
                $need = $energy[$i] - $en + 1;
                $ans += $need;
                $en += $need;
            }
            if ($ex <= $experience[$i]) {
                $need = $experience[$i] - $ex + 1;
                $ans += $need;
                $ex += $need;
            }
            $en -= $energy[$i];
            $ex += $experience[$i];
        }
        return $ans;
    }
}
