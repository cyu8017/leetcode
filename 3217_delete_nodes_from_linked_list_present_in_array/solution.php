<?php
// LeetCode 3217 - Delete Nodes From Linked List Present in Array
// https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    function modifiedList($nums, $head) {
        $s = [];
        foreach ($nums as $x) $s[$x] = true;
        $dummy = new ListNode(0, $head);
        $pre = $dummy;
        while ($pre->next !== null) {
            if (isset($s[$pre->next->val])) $pre->next = $pre->next->next;
            else $pre = $pre->next;
        }
        return $dummy->next;
    }
}
