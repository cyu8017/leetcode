<?php
// LeetCode 2130 - Maximum Twin Sum of a Linked List
// https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

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
     * @return Integer
     */
    function pairSum($head) {
        $slow = $head;
        $fast = $head;
        while ($fast !== null && $fast->next !== null) {
            $slow = $slow->next;
            $fast = $fast->next->next;
        }
        $prev = null;
        while ($slow !== null) {
            $nxt = $slow->next;
            $slow->next = $prev;
            $prev = $slow;
            $slow = $nxt;
        }
        $ans = 0;
        $a = $head;
        $b = $prev;
        while ($b !== null) {
            $ans = max($ans, $a->val + $b->val);
            $a = $a->next;
            $b = $b->next;
        }
        return $ans;
    }
}
