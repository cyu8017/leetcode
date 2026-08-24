<?php
// LeetCode 3155 - Maximum Number of Upgradable Servers
// https://leetcode.com/problems/maximum-number-of-upgradable-servers/

class Solution {
    function maxUpgrades($count, $upgrade, $sell, $money) {
        $ans = [];
        for ($i = 0; $i < count($count); $i++) {
            $cnt = $count[$i];
            $ans[$i] = min($cnt, intdiv($cnt * $sell[$i] + $money[$i], $upgrade[$i] + $sell[$i]));
        }
        return $ans;
    }
}
