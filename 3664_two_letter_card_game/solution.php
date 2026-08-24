<?php
// LeetCode 3664 - Two-Letter Card Game
// https://leetcode.com/problems/two-letter-card-game/

class Solution {
    function score($cards, $x) {
        $pairGroup = function($arr) {
            $total = 0;
            $mx = 0;
            for ($i = 0; $i < 26; $i++) {
                $total += $arr[$i];
                $mx = max($mx, $arr[$i]);
            }
            $pairs = intdiv($total, 2);
            if ($total - $mx < $pairs) $pairs = $total - $mx;
            return [$pairs, $total - 2 * $pairs];
        };
        $xx = 0;
        $left = array_fill(0, 26, 0);
        $right = array_fill(0, 26, 0);
        foreach ($cards as $c) {
            $a = $c[0];
            $b = $c[1];
            if ($a === $x && $b === $x) $xx++;
            else if ($a === $x) $left[ord($b) - 97]++;
            else if ($b === $x) $right[ord($a) - 97]++;
        }
        $lp = $pairGroup($left);
        $rp = $pairGroup($right);
        $ans = $lp[0] + $rp[0];
        $rem = $lp[1] + $rp[1];
        $use = min($xx, $rem);
        $ans += $use;
        $xx -= $use;
        $ans += intdiv($xx, 2);
        return $ans;
    }
}
