<?php
// LeetCode 1786 - Number of Restricted Paths From First to Last Node
// https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Integer
     */
    function countRestrictedPaths($n, $edges) {
        $adj = array_fill(0, $n + 1, []);
        foreach ($edges as $e) {
            $adj[$e[0]][] = [$e[1], $e[2]];
            $adj[$e[1]][] = [$e[0], $e[2]];
        }
        $dist = array_fill(0, $n + 1, PHP_INT_MAX);
        $dist[$n] = 0;
        $heap = new SplPriorityQueue();
        $heap->setExtractFlags(SplPriorityQueue::EXTR_BOTH);
        $heap->insert($n, 0);
        while (!$heap->isEmpty()) {
            $item = $heap->extract();
            $u = $item['data'];
            $d = -$item['priority'];
            if ($d !== $dist[$u]) {
                continue;
            }
            foreach ($adj[$u] as [$v, $w]) {
                $nd = $d + $w;
                if ($nd < $dist[$v]) {
                    $dist[$v] = $nd;
                    $heap->insert($v, -$nd);
                }
            }
        }
        $order = range(1, $n);
        usort($order, fn($a, $b) => $dist[$a] <=> $dist[$b]);
        $mod = 1000000007;
        $cnt = array_fill(0, $n + 1, 0);
        $cnt[$n] = 1;
        foreach ($order as $u) {
            if ($u === $n) {
                continue;
            }
            foreach ($adj[$u] as [$v, $w]) {
                if ($dist[$u] > $dist[$v]) {
                    $cnt[$u] = ($cnt[$u] + $cnt[$v]) % $mod;
                }
            }
        }
        return $cnt[1];
    }
}
