<?php
// LeetCode 3063 - Linked List Frequency
// https://leetcode.com/problems/linked-list-frequency/

class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    function frequenciesOfElements($head) {
        $cnt = [];
        for (; $head !== null; $head = $head->next) {
            $v = $head->val;
            $cnt[$v] = ($cnt[$v] ?? 0) + 1;
        }
        $dummy = new ListNode(0);
        foreach ($cnt as $val) {
            $dummy->next = new ListNode($val, $dummy->next);
        }
        return $dummy->next;
    }
}
