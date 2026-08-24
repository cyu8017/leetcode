<?php
// LeetCode 2764 - Is Array a Preorder of Some Binary Tree
// https://leetcode.com/problems/is-array-a-preorder-of-some-binary-tree/

class Solution {
    function isPreorder($nodes) {
        if (!$nodes) return true;
        $stack = [$nodes[0][0]];
        for ($i = 1; $i < count($nodes); $i++) {
            $id = $nodes[$i][0];
            $parent = $nodes[$i][1];
            while ($stack && $stack[count($stack) - 1] !== $parent) array_pop($stack);
            if (!$stack) return false;
            $stack[] = $id;
        }
        return true;
    }
}
