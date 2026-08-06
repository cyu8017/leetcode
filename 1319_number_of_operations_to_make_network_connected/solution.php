<?php
class Solution {
    function makeConnected($n, $connections) {
        if (count($connections) < $n - 1) return -1;
        $parent = range(0, $n - 1);
        $find = function($x) use (&$parent, &$find) {
            while ($x !== $parent[$x]) {
                $parent[$x] = $parent[$parent[$x]];
                $x = $parent[$x];
            }
            return $x;
        };
        foreach ($connections as [$a, $b]) {
            $ra = $find($a);
            $rb = $find($b);
            if ($ra !== $rb) $parent[$ra] = $rb;
        }
        $roots = [];
        for ($i = 0; $i < $n; $i++) $roots[$find($i)] = true;
        return count($roots) - 1;
    }
}
