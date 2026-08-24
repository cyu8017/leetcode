<?php
// LeetCode 0082 - Remove Duplicates from Sorted List II
// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

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
    function deleteDuplicates($head) {
        $dummy = new ListNode(0, $head);
        $previous = $dummy;

        while ($head) {
            if ($head->next && $head->val === $head->next->val) {
                while ($head->next && $head->val === $head->next->val) {
                    $head = $head->next;
                }
                $previous->next = $head->next;
            } else {
                $previous = $previous->next;
            }
            $head = $head->next;
        }

        return $dummy->next;
    }
}
