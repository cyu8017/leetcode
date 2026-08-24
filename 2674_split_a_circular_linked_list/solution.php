<?php
// LeetCode 2674 - Split a Circular Linked List
// https://leetcode.com/problems/split-a-circular-linked-list/

class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    function splitCircularLinkedList($list) {
        if ($list === null) return [null, null];
        $slow = $list;
        $fast = $list;
        while ($fast->next !== $list && $fast->next->next !== $list) {
            $slow = $slow->next;
            $fast = $fast->next->next;
        }
        if ($fast->next->next === $list) $fast = $fast->next;
        $head2 = $slow->next;
        $slow->next = $list;
        $fast->next = $head2;
        return [$list, $head2];
    }
}
