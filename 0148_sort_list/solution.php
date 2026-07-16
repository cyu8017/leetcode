<?php

class ListNode {
    public int $val;
    public ?ListNode $next;

    function __construct(int $val = 0, ?ListNode $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    function sortList(?ListNode $head): ?ListNode {
        if ($head === null || $head->next === null) {
            return $head;
        }

        $slow = $head;
        $fast = $head;
        $previous = null;
        while ($fast !== null && $fast->next !== null) {
            $previous = $slow;
            $slow = $slow->next;
            $fast = $fast->next->next;
        }
        $previous->next = null;

        return $this->merge($this->sortList($head), $this->sortList($slow));
    }

    private function merge(?ListNode $left, ?ListNode $right): ?ListNode {
        $dummy = new ListNode(0);
        $tail = $dummy;
        while ($left !== null && $right !== null) {
            if ($left->val <= $right->val) {
                $tail->next = $left;
                $left = $left->next;
            } else {
                $tail->next = $right;
                $right = $right->next;
            }
            $tail = $tail->next;
        }
        $tail->next = $left ?? $right;
        return $dummy->next;
    }
}