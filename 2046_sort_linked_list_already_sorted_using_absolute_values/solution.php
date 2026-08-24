<?php
// LeetCode 2046 - Sort Linked List Already Sorted Using Absolute Values
// https://leetcode.com/problems/sort-linked-list-already-sorted-using-absolute-values/

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
    function sortLinkedList($head) {
        if ($head === null) return null;
        $prev = $head;
        $cur = $head->next;
        while ($cur) {
            if ($cur->val < 0) {
                $prev->next = $cur->next;
                $cur->next = $head;
                $head = $cur;
                $cur = $prev->next;
            } else {
                $prev = $cur;
                $cur = $cur->next;
            }
        }
        return $head;
    }
}
