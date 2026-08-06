<?php
class Solution {
    function frogPosition($n, $edges, $t, $target) {
        $g = array_fill(0, $n + 1, []);
        foreach ($edges as [$a, $b]) {
            $g[$a][] = $b;
            $g[$b][] = $a;
        }
        $dfs = function($u, $p, $time, $prob) use (&$dfs, $g, $t, $target) {
            $kids = [];
            foreach ($g[$u] as $v) if ($v !== $p) $kids[] = $v;
            if ($time === $t || !$kids) return $u === $target ? $prob : 0.0;
            $sum = 0.0;
            foreach ($kids as $v) $sum += $dfs($v, $u, $time + 1, $prob / count($kids));
            return $sum;
        };
        return $dfs(1, 0, 0, 1.0);
    }
}
