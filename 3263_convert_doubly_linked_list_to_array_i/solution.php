<?php
// LeetCode 3263 - Convert Doubly Linked List to Array I
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-i/

class ListNode {
    public $val = 0;
    public $prev = null;
    public $next = null;
    function __construct($val = 0) {
        $this->val = $val;
    }
}

class Solution {
    function toArray($head) {
        $ans = [];
        while ($head !== null) {
            $ans[] = $head->val;
            $head = $head->next;
        }
        return $ans;
    }
}
