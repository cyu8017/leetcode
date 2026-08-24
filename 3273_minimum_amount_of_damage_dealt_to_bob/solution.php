<?php
// LeetCode 3273 - Minimum Amount of Damage Dealt to Bob
// https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/

class Solution {
    function minDamage($power, $damage, $health) {
        $n = count($damage);
        $arr = [];
        $totalDmg = 0;
        for ($i = 0; $i < $n; $i++) {
            $hits = intdiv($health[$i] + $power - 1, $power);
            $arr[] = [$damage[$i], $hits];
            $totalDmg += $damage[$i];
        }
        usort($arr, function($a, $b) {
            return $a[1] * $b[0] <=> $b[1] * $a[0];
        });
        $ans = 0;
        $cur = $totalDmg;
        foreach ($arr as $e) {
            $ans += $cur * $e[1];
            $cur -= $e[0];
        }
        return $ans;
    }
}
