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
    function insertionSortList(?ListNode $head): ?ListNode {
        $dummy = new ListNode(0);
        $current = $head;

        while ($current !== null) {
            $previous = $dummy;
            while ($previous->next !== null && $previous->next->val < $current->val) {
                $previous = $previous->next;
            }
            $next = $current->next;
            $current->next = $previous->next;
            $previous->next = $current;
            $current = $next;
        }
        return $dummy->next;
    }
}