<?php
// LeetCode 1810 - Minimum Path Cost in a Hidden Grid
// https://leetcode.com/problems/minimum-path-cost-in-a-hidden-grid/

class Solution {
    /** @var array<string, array{0: int, 1: int}> */
    private static $DIRS = [
        'U' => [-1, 0],
        'D' => [1, 0],
        'L' => [0, -1],
        'R' => [0, 1],
    ];
    /** @var array<string, string> */
    private static $OPP = ['U' => 'D', 'D' => 'U', 'L' => 'R', 'R' => 'L'];

    /**
     * @param object $master
     * @return Integer
     */
    function findShortestPath($master) {
        $moveCost = ['0,0' => 0];
        $target = null;

        if ($master->isTarget()) {
            return 0;
        }

        $this->dfs($master, 0, 0, $moveCost, $target);
        if ($target === null) {
            return -1;
        }

        $best = ['0,0' => 0];
        $heap = new SplMinHeap();
        $heap->insert([0, 0, 0]);

        while (!$heap->isEmpty()) {
            [$dist, $r, $c] = $heap->extract();
            $key = "$r,$c";
            if ($key === $target) {
                return $dist;
            }
            if ($dist > ($best[$key] ?? PHP_INT_MAX)) {
                continue;
            }
            foreach (self::$DIRS as $delta) {
                $nr = $r + $delta[0];
                $nc = $c + $delta[1];
                $nkey = "$nr,$nc";
                if (!isset($moveCost[$nkey])) {
                    continue;
                }
                $nd = $dist + $moveCost[$nkey];
                if ($nd < ($best[$nkey] ?? PHP_INT_MAX)) {
                    $best[$nkey] = $nd;
                    $heap->insert([$nd, $nr, $nc]);
                }
            }
        }
        return -1;
    }

    private function dfs($master, $r, $c, &$moveCost, &$target) {
        foreach (self::$DIRS as $direction => $delta) {
            if (!$master->canMove($direction)) {
                continue;
            }
            $cost = $master->move($direction);
            $nr = $r + $delta[0];
            $nc = $c + $delta[1];
            $key = "$nr,$nc";
            if (!isset($moveCost[$key])) {
                $moveCost[$key] = $cost;
                if ($master->isTarget()) {
                    $target = $key;
                }
                $this->dfs($master, $nr, $nc, $moveCost, $target);
            }
            $master->move(self::$OPP[$direction]);
        }
    }
}
