<?php
// LeetCode 0024 - Swap Nodes in Pairs
// https://leetcode.com/problems/swap-nodes-in-pairs/

class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    /**
     * @param ListNode $head
     * @return ListNode
     */
    function swapPairs($head) {
        $dummy = new ListNode(0, $head);
        $previous = $dummy;

        while ($previous->next && $previous->next->next) {
            $first = $previous->next;
            $second = $first->next;
            $first->next = $second->next;
            $second->next = $first;
            $previous->next = $second;
            $previous = $first;
        }

        return $dummy->next;
    }
}
