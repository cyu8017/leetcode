<?php
// LeetCode 2487 - Remove Nodes From Linked List
// https://leetcode.com/problems/remove-nodes-from-linked-list/

class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    function removeNodes($head) {
        $rev = function ($node) {
            $prev = null;
            while ($node !== null) {
                $nxt = $node->next;
                $node->next = $prev;
                $prev = $node;
                $node = $nxt;
            }
            return $prev;
        };
        $head = $rev($head);
        $mx = 0;
        $dummy = new ListNode(0, $head);
        $prev = $dummy;
        while ($prev->next !== null) {
            if ($prev->next->val >= $mx) {
                $mx = $prev->next->val;
                $prev = $prev->next;
            } else {
                $prev->next = $prev->next->next;
            }
        }
        return $rev($dummy->next);
    }
}
