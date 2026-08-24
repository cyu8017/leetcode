<?php
// LeetCode 2181 - Merge Nodes in Between Zeros
// https://leetcode.com/problems/merge-nodes-in-between-zeros/

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
    function mergeNodes($head) {
        $dummy = new ListNode();
        $cur = $dummy;
        $sum = 0;
        for ($p = $head->next; $p !== null; $p = $p->next) {
            if ($p->val === 0) {
                $cur->next = new ListNode($sum);
                $cur = $cur->next;
                $sum = 0;
            } else $sum += $p->val;
        }
        return $dummy->next;
    }
}
