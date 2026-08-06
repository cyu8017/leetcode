<?php
// LeetCode 1222 - Queens That Can Attack the King
// https://leetcode.com/problems/queens-that-can-attack-the-king/

class Solution {
    /**
     * @param Integer[][] $queens
     * @param Integer[] $king
     * @return Integer[][]
     */
    function queensAttacktheKing($queens, $king) {
        $occupied = [];
        foreach ($queens as $q) $occupied[$q[0] . ',' . $q[1]] = true;
        $answer = [];
        foreach ([-1, 0, 1] as $dr) {
            foreach ([-1, 0, 1] as $dc) {
                if ($dr === 0 && $dc === 0) continue;
                $r = $king[0] + $dr; $c = $king[1] + $dc;
                while ($r >= 0 && $r < 8 && $c >= 0 && $c < 8) {
                    if (isset($occupied["$r,$c"])) {
                        $answer[] = [$r, $c];
                        break;
                    }
                    $r += $dr; $c += $dc;
                }
            }
        }
        return $answer;
    }
}
