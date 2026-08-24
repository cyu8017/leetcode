<?php
// LeetCode 0083 - Remove Duplicates from Sorted List
// https://leetcode.com/problems/remove-duplicates-from-sorted-list/

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
        $current = $head;

        while ($current && $current->next) {
            if ($current->val === $current->next->val) {
                $current->next = $current->next->next;
            } else {
                $current = $current->next;
            }
        }

        return $head;
    }
}
