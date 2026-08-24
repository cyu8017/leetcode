<?php
// LeetCode 2508 - Add Edges to Make Degrees of All Nodes Even
// https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/

class Solution {
    function isPossible($n, $edges) {
        $deg = array_fill(0, $n + 1, 0);
        $adj = array_fill(0, $n + 1, []);
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $deg[$u]++;
            $deg[$v]++;
            $adj[$u][$v] = true;
            $adj[$v][$u] = true;
        }
        $odd = [];
        for ($i = 1; $i <= $n; $i++) if ($deg[$i] % 2 === 1) $odd[] = $i;
        if (count($odd) === 0) return true;
        if (count($odd) === 2) {
            $a = $odd[0];
            $b = $odd[1];
            if (!isset($adj[$a][$b])) return true;
            for ($i = 1; $i <= $n; $i++) {
                if ($i !== $a && $i !== $b && !isset($adj[$a][$i]) && !isset($adj[$b][$i])) return true;
            }
            return false;
        }
        if (count($odd) === 4) {
            $a = $odd[0];
            $b = $odd[1];
            $c = $odd[2];
            $d = $odd[3];
            return (!isset($adj[$a][$b]) && !isset($adj[$c][$d])) ||
                   (!isset($adj[$a][$c]) && !isset($adj[$b][$d])) ||
                   (!isset($adj[$a][$d]) && !isset($adj[$b][$c]));
        }
        return false;
    }
}
