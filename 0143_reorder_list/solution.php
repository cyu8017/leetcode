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
    function reorderList(?ListNode $head): void {
        if ($head === null || $head->next === null) {
            return;
        }

        $slow = $head;
        $fast = $head;
        while ($fast->next !== null && $fast->next->next !== null) {
            $slow = $slow->next;
            $fast = $fast->next->next;
        }

        $second = $slow->next;
        $slow->next = null;
        $previous = null;
        while ($second !== null) {
            $next = $second->next;
            $second->next = $previous;
            $previous = $second;
            $second = $next;
        }

        $first = $head;
        $second = $previous;
        while ($second !== null) {
            $firstNext = $first->next;
            $secondNext = $second->next;
            $first->next = $second;
            $second->next = $firstNext;
            $first = $firstNext;
            $second = $secondNext;
        }
    }
}