<?php
class Solution {
    function minTime($n, $edges, $hasApple) {
        $graph = array_fill(0, $n, []);
        foreach ($edges as [$a, $b]) {
            $graph[$a][] = $b;
            $graph[$b][] = $a;
        }
        $visit = function($node, $parent) use (&$visit, $graph, $hasApple) {
            $cost = 0;
            foreach ($graph[$node] as $child) {
                if ($child !== $parent) {
                    $childCost = $visit($child, $node);
                    if ($childCost || $hasApple[$child]) $cost += $childCost + 2;
                }
            }
            return $cost;
        };
        return $visit(0, -1);
    }
}
