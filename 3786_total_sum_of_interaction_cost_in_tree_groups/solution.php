<?php
// LeetCode 3786 - Total Sum of Interaction Cost in Tree Groups
// https://leetcode.com/problems/total-sum-of-interaction-cost-in-tree-groups/

class Solution {
    function interactionCost($n, $edges, $group) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $total = array_fill(0, 21, 0);
        foreach ($group as $x) $total[$x]++;
        $parent = array_fill(0, $n, -2);
        $parent[0] = -1;
        $order = [0];
        for ($i = 0; $i < count($order); $i++) {
            $u = $order[$i];
            foreach ($g[$u] as $v) {
                if ($parent[$v] === -2) {
                    $parent[$v] = $u;
                    $order[] = $v;
                }
            }
        }
        $count = [];
        for ($i = 0; $i < $n; $i++) $count[$i] = array_fill(0, 21, 0);
        $ans = 0;
        for ($i = $n - 1; $i >= 0; $i--) {
            $u = $order[$i];
            $count[$u][$group[$u]]++;
            foreach ($g[$u] as $v) {
                if ($parent[$v] !== $u) continue;
                for ($c = 1; $c <= 20; $c++) {
                    $x = $count[$v][$c];
                    $ans += $x * ($total[$c] - $x);
                    $count[$u][$c] += $x;
                }
            }
        }
        return $ans;
    }
}
