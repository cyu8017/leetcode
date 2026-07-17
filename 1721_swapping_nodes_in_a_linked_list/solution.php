<?php
// LeetCode 1721 - Swapping Nodes in a Linked List
// https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

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
     * @param Integer $k
     * @return ListNode
     */
    function swapNodes($head, $k) {
        $first = $head;
        for ($i = 0; $i < $k - 1; $i++) {
            $first = $first->next;
        }
        $fast = $first;
        $second = $head;
        while ($fast->next !== null) {
            $fast = $fast->next;
            $second = $second->next;
        }
        $temp = $first->val;
        $first->val = $second->val;
        $second->val = $temp;
        return $head;
    }
}
