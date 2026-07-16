<?php

// LeetCode 0234 - Palindrome Linked List
// https://leetcode.com/problems/palindrome-linked-list/

class ListNode {
    public $val;
    public $next;

    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    function isPalindrome($head) {
        if ($head === null || $head->next === null) {
            return true;
        }

        $slow = $head;
        $fast = $head;
        while ($fast !== null && $fast->next !== null) {
            $slow = $slow->next;
            $fast = $fast->next->next;
        }

        $prev = null;
        while ($slow !== null) {
            $next = $slow->next;
            $slow->next = $prev;
            $prev = $slow;
            $slow = $next;
        }

        $left = $head;
        $right = $prev;
        while ($right !== null) {
            if ($left->val !== $right->val) {
                return false;
            }
            $left = $left->next;
            $right = $right->next;
        }
        return true;
    }
}
