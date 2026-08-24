<?php
// LeetCode 2363 - Merge Similar Items
// https://leetcode.com/problems/merge-similar-items/

class Solution {
    function mergeSimilarItems($items1, $items2) {
        $mp = [];
        foreach ($items1 as $it) $mp[$it[0]] = ($mp[$it[0]] ?? 0) + $it[1];
        foreach ($items2 as $it) $mp[$it[0]] = ($mp[$it[0]] ?? 0) + $it[1];
        ksort($mp);
        $ans = [];
        foreach ($mp as $k => $v) $ans[] = [$k, $v];
        return $ans;
    }
}
