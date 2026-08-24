<?php
// LeetCode 0002 - Add Two Numbers
// https://leetcode.com/problems/add-two-numbers/

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
     * @param ListNode $l1
     * @param ListNode $l2
     * @return ListNode
     */
    function addTwoNumbers($l1, $l2) {
        $dummy = new ListNode();
        $current = $dummy;
        $carry = 0;

        while ($l1 || $l2 || $carry) {
            $total = $carry;
            if ($l1) {
                $total += $l1->val;
                $l1 = $l1->next;
            }
            if ($l2) {
                $total += $l2->val;
                $l2 = $l2->next;
            }
            $carry = intdiv($total, 10);
            $current->next = new ListNode($total % 10);
            $current = $current->next;
        }

        return $dummy->next;
    }
}
