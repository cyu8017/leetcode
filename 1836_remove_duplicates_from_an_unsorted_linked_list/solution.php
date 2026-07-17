<?php
// LeetCode 1836 - Remove Duplicates From an Unsorted Linked List
// https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/

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
    function deleteDuplicatesUnsorted($head) {
        $counts = [];
        $node = $head;
        while ($node !== null) {
            $counts[$node->val] = ($counts[$node->val] ?? 0) + 1;
            $node = $node->next;
        }

        $dummy = new ListNode(0, $head);
        $prev = $dummy;
        $node = $head;
        while ($node !== null) {
            if ($counts[$node->val] > 1) {
                $prev->next = $node->next;
                $node = $node->next;
            } else {
                $prev = $node;
                $node = $node->next;
            }
        }
        return $dummy->next;
    }
}
