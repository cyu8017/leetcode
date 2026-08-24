<?php
// LeetCode 0206 - Reverse Linked List
// https://leetcode.com/problems/reverse-linked-list/

class ListNode {
    public $val;
    public $next;

    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    function reverseList($head) {
        $previous = null;
        $current = $head;
        while ($current !== null) {
            $next = $current->next;
            $current->next = $previous;
            $previous = $current;
            $current = $next;
        }
        return $previous;
    }
}
