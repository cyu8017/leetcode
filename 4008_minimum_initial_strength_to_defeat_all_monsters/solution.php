<?php
// LeetCode 4008 - Minimum Initial Strength to Defeat All Monsters
// https://leetcode.com/problems/minimum-initial-strength-to-defeat-all-monsters/

class Solution {
    function minInitialStrength($monsters, $boosts) {
        $n = count($monsters);
        $d = array_fill(0, $n + 1, 0);
        foreach ($boosts as $b) {
            $d[$b[0]] += $b[2];
            $d[$b[1] + 1] -= $b[2];
        }
        $left = 0;
        $right = 1000000000000000;
        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            if ($this->check($mid, $monsters, $d)) $right = $mid;
            else $left = $mid + 1;
        }
        return $left;
    }

    private function check($v, $monsters, $d) {
        $bonus = 0;
        for ($i = 0; $i < count($monsters); $i++) {
            $bonus += $d[$i];
            if ($v + $bonus < $monsters[$i]) return false;
            $v -= $monsters[$i];
            if ($v < 0) $v = 0;
        }
        return true;
    }
}
