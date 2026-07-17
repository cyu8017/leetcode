<?php
// LeetCode 1778 - Shortest Path in a Hidden Grid
// https://leetcode.com/problems/shortest-path-in-a-hidden-grid/

class Solution {
    private $grid;
    private $m;
    private $n;
    private $r;
    private $c;
    private $world;
    private $target;

    private static $DIR = [
        'U' => [-1, 0],
        'D' => [1, 0],
        'L' => [0, -1],
        'R' => [0, 1],
    ];
    private static $OPP = ['U' => 'D', 'D' => 'U', 'L' => 'R', 'R' => 'L'];

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function findShortestPath($grid) {
        $this->grid = $grid;
        $this->m = count($grid);
        $this->n = count($grid[0]);
        $this->r = 0;
        $this->c = 0;
        for ($i = 0; $i < $this->m; $i++) {
            for ($j = 0; $j < $this->n; $j++) {
                if ($grid[$i][$j] === -1) {
                    $this->r = $i;
                    $this->c = $j;
                }
            }
        }

        $this->world = ['0,0' => 1];
        $this->target = null;
        if ($this->isTarget()) {
            return 0;
        }

        $this->dfs(0, 0);
        if ($this->target === null) {
            return -1;
        }

        $queue = [[0, 0, 0]];
        $seen = ['0,0' => true];
        while (!empty($queue)) {
            [$cr, $cc, $dist] = array_shift($queue);
            if ("$cr,$cc" === $this->target) {
                return $dist;
            }
            foreach (self::$DIR as $d) {
                $nr = $cr + $d[0];
                $nc = $cc + $d[1];
                $key = "$nr,$nc";
                if (isset($this->world[$key]) && !isset($seen[$key])) {
                    $seen[$key] = true;
                    $queue[] = [$nr, $nc, $dist + 1];
                }
            }
        }
        return -1;
    }

    private function canMove($d) {
        $nr = $this->r + self::$DIR[$d][0];
        $nc = $this->c + self::$DIR[$d][1];
        return $nr >= 0 && $nr < $this->m && $nc >= 0 && $nc < $this->n
            && $this->grid[$nr][$nc] !== 0;
    }

    private function move($d) {
        if ($this->canMove($d)) {
            $this->r += self::$DIR[$d][0];
            $this->c += self::$DIR[$d][1];
        }
    }

    private function isTarget() {
        return $this->grid[$this->r][$this->c] === 2;
    }

    private function dfs($cr, $cc) {
        foreach (self::$DIR as $d => $delta) {
            if (!$this->canMove($d)) {
                continue;
            }
            $this->move($d);
            $nr = $cr + $delta[0];
            $nc = $cc + $delta[1];
            $key = "$nr,$nc";
            if (!isset($this->world[$key])) {
                $this->world[$key] = $this->isTarget() ? 2 : 1;
                if ($this->isTarget()) {
                    $this->target = $key;
                }
                $this->dfs($nr, $nc);
            }
            $this->move(self::$OPP[$d]);
        }
    }
}
