<?php
// LeetCode 0913 - Cat and Mouse
// https://leetcode.com/problems/cat-and-mouse/

class Solution {
    function catMouseGame($graph) {
        $n = count($graph);
        $DRAW = 0;
        $MOUSE_WIN = 1;
        $CAT_WIN = 2;
        $states = [];
        $outDegree = [];
        for ($cat = 0; $cat < $n; $cat++) {
            $states[$cat] = [];
            $outDegree[$cat] = [];
            for ($mouse = 0; $mouse < $n; $mouse++) {
                $states[$cat][$mouse] = [0, 0];
                $outDegree[$cat][$mouse] = [count($graph[$mouse]), 0];
                $deg = 0;
                foreach ($graph[$cat] as $x) if ($x !== 0) $deg++;
                $outDegree[$cat][$mouse][1] = $deg;
            }
        }
        $q = [];
        for ($cat = 1; $cat < $n; $cat++) {
            for ($move = 0; $move < 2; $move++) {
                $states[$cat][0][$move] = $MOUSE_WIN;
                $q[] = [$cat, 0, $move, $MOUSE_WIN];
                $states[$cat][$cat][$move] = $CAT_WIN;
                $q[] = [$cat, $cat, $move, $CAT_WIN];
            }
        }
        while ($q) {
            [$cat, $mouse, $move, $state] = array_shift($q);
            if ($cat === 2 && $mouse === 1 && $move === 0) return $state;
            $prevMove = $move ^ 1;
            foreach ($graph[$prevMove === 1 ? $cat : $mouse] as $prev) {
                $prevCat = $prevMove === 1 ? $prev : $cat;
                if ($prevCat === 0) continue;
                $prevMouse = $prevMove === 1 ? $mouse : $prev;
                if ($states[$prevCat][$prevMouse][$prevMove] !== 0) continue;
                if (($prevMove === 0 && $state === $MOUSE_WIN) ||
                    ($prevMove === 1 && $state === $CAT_WIN) ||
                    $outDegree[$prevCat][$prevMouse][$prevMove] === 1) {
                    $states[$prevCat][$prevMouse][$prevMove] = $state;
                    $q[] = [$prevCat, $prevMouse, $prevMove, $state];
                } else {
                    $outDegree[$prevCat][$prevMouse][$prevMove]--;
                }
            }
        }
        return $states[2][1][0];
    }
}
