<?php
// LeetCode 2649 - Nested Array Generator
// https://leetcode.com/problems/nested-array-generator/

class Solution {
    function inorderTraversal($arr) {
        foreach ($arr as $x) {
            if (is_array($x)) {
                yield from $this->inorderTraversal($x);
            } else {
                yield $x;
            }
        }
    }
}
