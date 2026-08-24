<?php
// LeetCode 2603 - Collect Coins in a Tree
// https://leetcode.com/problems/collect-coins-in-a-tree/

class Solution {
    function collectTheCoins($coins, $edges) {
        $n = count($coins);
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][$e[1]] = true;
            $g[$e[1]][$e[0]] = true;
        }
        $deg = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) $deg[$i] = count($g[$i]);
        $q = [];
        for ($i = 0; $i < $n; $i++) {
            if ($deg[$i] === 1 && $coins[$i] === 0) $q[] = $i;
        }
        while ($q) {
            $u = array_shift($q);
            foreach (array_keys($g[$u]) as $v) {
                unset($g[$v][$u]);
                $deg[$v]--;
                if ($deg[$v] === 1 && $coins[$v] === 0) $q[] = $v;
            }
            $g[$u] = [];
            $deg[$u] = 0;
        }
        for ($round = 0; $round < 2; $round++) {
            $leaves = [];
            for ($i = 0; $i < $n; $i++) if ($deg[$i] === 1) $leaves[] = $i;
            foreach ($leaves as $u) {
                foreach (array_keys($g[$u]) as $v) {
                    unset($g[$v][$u]);
                    $deg[$v]--;
                }
                $g[$u] = [];
                $deg[$u] = 0;
            }
        }
        $remain = 0;
        for ($i = 0; $i < $n; $i++) $remain += count($g[$i]);
        return $remain;
    }
}
