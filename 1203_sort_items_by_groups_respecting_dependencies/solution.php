<?php
// LeetCode 1203 - Sort Items by Groups Respecting Dependencies
// https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

class Solution {
    /**
     * @param Integer $n
     * @param Integer $m
     * @param Integer[] $group
     * @param Integer[][] $beforeItems
     * @return Integer[]
     */
    function sortItems($n, $m, $group, $beforeItems) {
        for ($i = 0; $i < $n; $i++) {
            if ($group[$i] === -1) {
                $group[$i] = $m;
                $m++;
            }
        }
        $itemGraph = array_fill(0, $n, []);
        $itemIndeg = array_fill(0, $n, 0);
        $groupGraph = array_fill(0, $m, []);
        $groupIndeg = array_fill(0, $m, 0);
        $groupSeen = array_fill(0, $m, []);
        for ($v = 0; $v < $n; $v++) {
            foreach ($beforeItems[$v] as $u) {
                $itemGraph[$u][] = $v;
                $itemIndeg[$v]++;
                if ($group[$u] !== $group[$v] && !isset($groupSeen[$group[$u]][$group[$v]])) {
                    $groupSeen[$group[$u]][$group[$v]] = true;
                    $groupGraph[$group[$u]][] = $group[$v];
                    $groupIndeg[$group[$v]]++;
                }
            }
        }
        $topo = function ($graph, $indeg) {
            $queue = [];
            foreach ($indeg as $i => $d) if ($d === 0) $queue[] = $i;
            $order = [];
            $head = 0;
            while ($head < count($queue)) {
                $u = $queue[$head++];
                $order[] = $u;
                foreach ($graph[$u] as $v) {
                    if (--$indeg[$v] === 0) $queue[] = $v;
                }
            }
            return count($order) === count($graph) ? $order : [];
        };
        $items = $topo($itemGraph, $itemIndeg);
        $groups = $topo($groupGraph, $groupIndeg);
        if (empty($items) || empty($groups)) return [];
        $buckets = array_fill(0, $m, []);
        foreach ($items as $item) $buckets[$group[$item]][] = $item;
        $ans = [];
        foreach ($groups as $g) foreach ($buckets[$g] as $item) $ans[] = $item;
        return $ans;
    }
}
