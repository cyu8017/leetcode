<?php
// LeetCode 2003 - Smallest Missing Genetic Value in Each Subtree
// https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/

class Solution {
    /**
     * @param Integer[] $parents
     * @param Integer[] $nums
     * @return Integer[]
     */
    function smallestMissingValueSubtree($parents, $nums) {
        $n = count($parents);
        $children = array_fill(0, $n, []);
        for ($i = 1; $i < $n; $i++) $children[$parents[$i]][] = $i;
        $ans = array_fill(0, $n, 1);
        $one = -1;
        for ($i = 0; $i < $n; $i++) if ($nums[$i] === 1) { $one = $i; break; }
        if ($one < 0) return $ans;
        $seen = [];
        $collect = null;
        $collect = function ($u) use (&$collect, &$seen, &$children, $nums) {
            if (isset($seen[$nums[$u]])) return;
            $seen[$nums[$u]] = true;
            foreach ($children[$u] as $v) $collect($v);
        };
        $miss = 1;
        $node = $one;
        $prev = -1;
        while ($node !== -1) {
            foreach ($children[$node] as $v) if ($v !== $prev) $collect($v);
            $seen[$nums[$node]] = true;
            while (isset($seen[$miss])) $miss++;
            $ans[$node] = $miss;
            $prev = $node;
            $node = $parents[$node];
        }
        return $ans;
    }
}
