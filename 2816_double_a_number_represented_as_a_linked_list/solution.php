<?php
// LeetCode 2816 - Double a Number Represented as a Linked List
// https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    function doubleIt($head) {
        $rev = function($node) {
            $prev = null;
            while ($node) {
                $nxt = $node->next;
                $node->next = $prev;
                $prev = $node;
                $node = $nxt;
            }
            return $prev;
        };
        $head = $rev($head);
        $carry = 0;
        $cur = $head;
        $prev = null;
        while ($cur) {
            $val = $cur->val * 2 + $carry;
            $cur->val = $val % 10;
            $carry = intdiv($val, 10);
            $prev = $cur;
            $cur = $cur->next;
        }
        if ($carry > 0) $prev->next = new ListNode($carry);
        return $rev($head);
    }
}
