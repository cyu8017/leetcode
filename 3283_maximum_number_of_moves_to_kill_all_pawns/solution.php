<?php
// LeetCode 3283 - Maximum Number of Moves to Kill All Pawns
// https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/

class Solution {
    private $dist;
    private $n;
    private $N;
    private $memo;

    function maxMoves($kx, $ky, $positions) {
        $this->n = count($positions);
        $n = $this->n;
        $pts = [];
        for ($i = 0; $i <= $n; $i++) $pts[$i] = [0, 0];
        $pts[0][0] = $kx;
        $pts[0][1] = $ky;
        for ($i = 0; $i < $n; $i++) {
            $pts[$i + 1][0] = $positions[$i][0];
            $pts[$i + 1][1] = $positions[$i][1];
        }
        $this->dist = [];
        for ($i = 0; $i <= $n; $i++) $this->dist[$i] = $this->knightDist($pts[$i][0], $pts[$i][1], $pts);
        $this->N = 1 << $n;
        $this->memo = [];
        for ($i = 0; $i < $this->N; $i++) $this->memo[$i] = array_fill(0, $n + 1, -1);
        return $this->dfs(0, 0, 0);
    }

    private function knightDist($x, $y, $pts) {
        $DIRS = [[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]];
        $np = count($pts);
        $ans = array_fill(0, $np, -1);
        $vis = [];
        for ($i = 0; $i < 50; $i++) $vis[$i] = array_fill(0, 50, false);
        $q = [[$x, $y, 0]];
        $vis[$x][$y] = true;
        $need = [];
        for ($i = 0; $i < $np; $i++) {
            $key = $pts[$i][0] . ',' . $pts[$i][1];
            if (!isset($need[$key])) $need[$key] = [];
            $need[$key][] = $i;
        }
        $found = 0;
        $qi = 0;
        while ($qi < count($q) && $found < $np) {
            $cur = $q[$qi++];
            $key = $cur[0] . ',' . $cur[1];
            if (isset($need[$key])) {
                foreach ($need[$key] as $i) {
                    if ($ans[$i] === -1) { $ans[$i] = $cur[2]; $found++; }
                }
            }
            foreach ($DIRS as $d) {
                $nx = $cur[0] + $d[0];
                $ny = $cur[1] + $d[1];
                if ($nx < 0 || $ny < 0 || $nx >= 50 || $ny >= 50 || $vis[$nx][$ny]) continue;
                $vis[$nx][$ny] = true;
                $q[] = [$nx, $ny, $cur[2] + 1];
            }
        }
        return $ans;
    }

    private function dfs($mask, $cur, $turn) {
        if ($mask === $this->N - 1) return 0;
        if ($this->memo[$mask][$cur] !== -1) return $this->memo[$mask][$cur];
        $best = $turn === 0 ? -(1 << 30) : (1 << 30);
        for ($i = 0; $i < $this->n; $i++) {
            if (($mask & (1 << $i)) !== 0) continue;
            $d = $this->dist[$cur][$i + 1];
            $v = $d + $this->dfs($mask | (1 << $i), $i + 1, 1 - $turn);
            if ($turn === 0) { if ($v > $best) $best = $v; }
            else if ($v < $best) $best = $v;
        }
        return $this->memo[$mask][$cur] = $best;
    }
}
