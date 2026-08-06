<?php
class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $roads
     * @return Integer
     */
    function countPaths($n, $roads) {
        $mod = 1000000007;
        $g = array_fill(0, $n, []);
        foreach ($roads as $r) {
            $g[$r[0]][] = [$r[1], $r[2]];
            $g[$r[1]][] = [$r[0], $r[2]];
        }
        $inf = PHP_INT_MAX;
        $dist = array_fill(0, $n, $inf);
        $ways = array_fill(0, $n, 0);
        $dist[0] = 0;
        $ways[0] = 1;
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_BOTH);
        $pq->insert(0, 0);
        while (!$pq->isEmpty()) {
            $item = $pq->extract();
            $u = $item['data'];
            $d = -$item['priority'];
            if ($d > $dist[$u]) {
                continue;
            }
            foreach ($g[$u] as [$v, $w]) {
                $nd = $d + $w;
                if ($nd < $dist[$v]) {
                    $dist[$v] = $nd;
                    $ways[$v] = $ways[$u];
                    $pq->insert($v, -$nd);
                } elseif ($nd === $dist[$v]) {
                    $ways[$v] = ($ways[$v] + $ways[$u]) % $mod;
                }
            }
        }
        return $ways[$n - 1];
    }
}
