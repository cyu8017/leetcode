<?php

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $roads
     * @param String[] $names
     * @param String[] $targetPath
     * @return Integer[]
     */
    function mostSimilar($n, $roads, $names, $targetPath) {
        $graph = array_fill(0, $n, []);
        foreach ($roads as $r) {
            $graph[$r[0]][] = $r[1];
            $graph[$r[1]][] = $r[0];
        }
        $dp = [];
        for ($node = 0; $node < $n; $node++) {
            $dp[$node] = [
                $names[$node] !== $targetPath[0] ? 1 : 0,
                [$node],
            ];
        }
        $len = count($targetPath);
        for ($i = 1; $i < $len; $i++) {
            $nextDp = [];
            for ($node = 0; $node < $n; $node++) {
                $bestCost = PHP_INT_MAX;
                $bestPath = null;
                foreach ($graph[$node] as $previous) {
                    $cand = $dp[$previous];
                    if ($cand[0] < $bestCost || ($cand[0] === $bestCost && $cand[1] < $bestPath)) {
                        $bestCost = $cand[0];
                        $bestPath = $cand[1];
                    }
                }
                $path = $bestPath;
                $path[] = $node;
                $nextDp[$node] = [
                    $bestCost + ($names[$node] !== $targetPath[$i] ? 1 : 0),
                    $path,
                ];
            }
            $dp = $nextDp;
        }
        $best = $dp[0];
        for ($node = 1; $node < $n; $node++) {
            if ($dp[$node][0] < $best[0] || ($dp[$node][0] === $best[0] && $dp[$node][1] < $best[1])) {
                $best = $dp[$node];
            }
        }
        return $best[1];
    }
}
