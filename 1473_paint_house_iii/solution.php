<?php
class Solution {
    function minCost($houses, $cost, $m, $n, $target) {
        $inf = 10 ** 15;
        $dp = ["0,0" => 0];
        foreach ($houses as $i => $painted) {
            $nxt = [];
            $colors = $painted ? [$painted] : range(1, $n);
            foreach ($dp as $key => $value) {
                [$prev, $groups] = array_map('intval', explode(",", $key));
                foreach ($colors as $color) {
                    $ng = $groups + ($color !== $prev ? 1 : 0);
                    if ($ng <= $target) {
                        $nv = $value + ($painted ? 0 : $cost[$i][$color - 1]);
                        $nk = "$color,$ng";
                        $nxt[$nk] = min($nxt[$nk] ?? $inf, $nv);
                    }
                }
            }
            $dp = $nxt;
        }
        $ans = $inf;
        foreach ($dp as $key => $v) {
            [, $g] = array_map('intval', explode(",", $key));
            if ($g === $target) $ans = min($ans, $v);
        }
        return $ans === $inf ? -1 : $ans;
    }
}
