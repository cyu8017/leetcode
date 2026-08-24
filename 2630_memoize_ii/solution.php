<?php
// LeetCode 2630 - Memoize II
// https://leetcode.com/problems/memoize-ii/

class Solution {
    function memoize($fn) {
        $root = [];
        $RES = '__res__';
        return function(...$args) use ($fn, &$root, $RES) {
            $node =& $root;
            foreach ($args as $a) {
                $k = is_scalar($a) ? gettype($a) . ':' . (string)$a : serialize($a);
                if (!isset($node[$k]) || !is_array($node[$k])) $node[$k] = [];
                $node =& $node[$k];
            }
            if (array_key_exists($RES, $node)) return $node[$RES];
            $v = $fn(...$args);
            $node[$RES] = $v;
            return $v;
        };
    }
}
