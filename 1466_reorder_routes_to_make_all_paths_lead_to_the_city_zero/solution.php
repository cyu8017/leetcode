<?php
class Solution {
    function minReorder($n, $connections) {
        $graph = array_fill(0, $n, []);
        foreach ($connections as [$a, $b]) {
            $graph[$a][] = [$b, 1];
            $graph[$b][] = [$a, 0];
        }
        $ans = 0;
        $stack = [0];
        $seen = [0 => true];
        while ($stack) {
            $node = array_pop($stack);
            foreach ($graph[$node] as [$nei, $cost]) {
                if (!isset($seen[$nei])) {
                    $seen[$nei] = true;
                    $stack[] = $nei;
                    $ans += $cost;
                }
            }
        }
        return $ans;
    }
}
