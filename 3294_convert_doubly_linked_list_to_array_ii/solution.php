<?php
// LeetCode 3294 - Convert Doubly Linked List to Array II
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/

class Node {
    public $val;
    public $prev;
    public $next;
    function __construct($val = 0, $prev = null, $next = null) {
        $this->val = $val;
        $this->prev = $prev;
        $this->next = $next;
    }
}

class Solution {
    function toArray($node) {
        while ($node !== null && $node->prev !== null) $node = $node->prev;
        $ans = [];
        while ($node !== null) {
            $ans[] = $node->val;
            $node = $node->next;
        }
        return $ans;
    }
}
