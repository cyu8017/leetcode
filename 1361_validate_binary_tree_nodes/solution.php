<?php
class Solution {
    function validateBinaryTreeNodes($n, $leftChild, $rightChild) {
        $indeg = array_fill(0, $n, 0);
        foreach (array_merge($leftChild, $rightChild) as $x) {
            if ($x !== -1) {
                $indeg[$x]++;
                if ($indeg[$x] > 1) return false;
            }
        }
        $roots = [];
        for ($i = 0; $i < $n; $i++) if ($indeg[$i] === 0) $roots[] = $i;
        if (count($roots) !== 1) return false;
        $seen = [];
        $st = $roots;
        while ($st) {
            $u = array_pop($st);
            if (isset($seen[$u])) return false;
            $seen[$u] = true;
            foreach ([$leftChild[$u], $rightChild[$u]] as $v) {
                if ($v !== -1) $st[] = $v;
            }
        }
        return count($seen) === $n;
    }
}
