<?php
// LeetCode 0092 - Reverse Linked List II
// https://leetcode.com/problems/reverse-linked-list-ii/

class ListNode {
    /** @var int */
    public $val = 0;
    /** @var ListNode|null */
    public $next = null;

    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    /**
     * @param ListNode|null $head
     * @param Integer $left
     * @param Integer $right
     * @return ListNode|null
     */
    function reverseBetween($head, $left, $right) {
        if ($head === null || $left === $right) {
            return $head;
        }

        $dummy = new ListNode(0, $head);
        $before = $dummy;
        for ($i = 0; $i < $left - 1; $i++) {
            $before = $before->next;
        }

        $start = $before->next;
        $current = $start->next;

        for ($i = 0; $i < $right - $left; $i++) {
            $start->next = $current->next;
            $current->next = $before->next;
            $before->next = $current;
            $current = $start->next;
        }

        return $dummy->next;
    }
}
