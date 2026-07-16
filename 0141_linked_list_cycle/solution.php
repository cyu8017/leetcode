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
    function hasCycle(?ListNode $head): bool {
        $slow = $head;
        $fast = $head;

        while ($fast !== null && $fast->next !== null) {
            $slow = $slow->next;
            $fast = $fast->next->next;
            if ($slow === $fast) {
                return true;
            }
        }
        return false;
    }
}