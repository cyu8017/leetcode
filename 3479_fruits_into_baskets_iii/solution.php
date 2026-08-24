<?php
// LeetCode 3479 - Fruits Into Baskets III
// https://leetcode.com/problems/fruits-into-baskets-iii/

class Solution {
    function numOfUnplacedFruits($fruits, $baskets) {
        $n = count($baskets);
        $size = 1;
        while ($size < $n) $size <<= 1;
        $tree = array_fill(0, $size * 2, 0);
        for ($i = 0; $i < $n; $i++) $tree[$size + $i] = $baskets[$i];
        for ($i = $size - 1; $i > 0; $i--) $tree[$i] = max($tree[$i * 2], $tree[$i * 2 + 1]);
        $find = null;
        $find = function($node, $nl, $nr, $need) use (&$find, &$tree) {
            if ($tree[$node] < $need) return -1;
            if ($nl === $nr) return $nl;
            $mid = intdiv($nl + $nr, 2);
            $left = $find($node * 2, $nl, $mid, $need);
            if ($left !== -1) return $left;
            return $find($node * 2 + 1, $mid + 1, $nr, $need);
        };
        $update = function($idx) use ($size, &$tree) {
            $p = $size + $idx;
            $tree[$p] = -1;
            for ($p >>= 1; $p > 0; $p >>= 1) $tree[$p] = max($tree[$p * 2], $tree[$p * 2 + 1]);
        };
        $unplaced = 0;
        foreach ($fruits as $f) {
            $idx = $find(1, 0, $size - 1, $f);
            if ($idx === -1 || $idx >= $n) $unplaced++;
            else $update($idx);
        }
        return $unplaced;
    }
}
