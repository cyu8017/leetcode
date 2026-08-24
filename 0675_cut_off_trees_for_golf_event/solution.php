<?php
// LeetCode 0675 - Cut Off Trees for Golf Event
// https://leetcode.com/problems/cut-off-trees-for-golf-event/

class Solution {
    function cutOffTree($forest) {
        $trees = [];
        for ($i = 0; $i < count($forest); ++$i) {
            for ($j = 0; $j < count($forest[0]); ++$j) {
                if ($forest[$i][$j] > 1) $trees[] = [$forest[$i][$j], $i, $j];
            }
        }
        usort($trees, function($a, $b) { return $a[0] <=> $b[0]; });
        $bfs = function($sr, $sc, $tr, $tc) use ($forest) {
            if ($sr === $tr && $sc === $tc) return 0;
            $m = count($forest);
            $n = count($forest[0]);
            $seen = [];
            for ($i = 0; $i < $m; ++$i) $seen[$i] = array_fill(0, $n, false);
            $queue = [[$sr, $sc, 0]];
            $seen[$sr][$sc] = true;
            $dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]];
            while ($queue) {
                $item = array_shift($queue);
                $r = $item[0]; $c = $item[1]; $dist = $item[2];
                foreach ($dirs as $d) {
                    $nr = $r + $d[0];
                    $nc = $c + $d[1];
                    if ($nr < 0 || $nr >= $m || $nc < 0 || $nc >= $n || $seen[$nr][$nc] || $forest[$nr][$nc] === 0) continue;
                    if ($nr === $tr && $nc === $tc) return $dist + 1;
                    $seen[$nr][$nc] = true;
                    $queue[] = [$nr, $nc, $dist + 1];
                }
            }
            return -1;
        };
        $sr = 0;
        $sc = 0;
        $steps = 0;
        foreach ($trees as $tree) {
            $dist = $bfs($sr, $sc, $tree[1], $tree[2]);
            if ($dist < 0) return -1;
            $steps += $dist;
            $sr = $tree[1];
            $sc = $tree[2];
        }
        return $steps;
    }
}
