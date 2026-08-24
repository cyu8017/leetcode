<?php
// LeetCode 0061 - Rotate List
// https://leetcode.com/problems/rotate-list/

class ListNode {
    /** @var int */
    public $val = 0;
    /** @var ListNode|null */
    public $next = null;

    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    /**
     * @param ListNode|null $head
     * @param Integer $k
     * @return ListNode|null
     */
    function rotateRight($head, $k) {
        if ($head === null || $head->next === null) {
            return $head;
        }

        $tail = $head;
        $length = 1;
        while ($tail->next !== null) {
            $tail = $tail->next;
            $length++;
        }

        $tail->next = $head;
        $k %= $length;
        if ($k === 0) {
            $tail->next = null;
            return $head;
        }

        $steps = $length - $k;
        $newTail = $head;
        for ($i = 0; $i < $steps - 1; $i++) {
            $newTail = $newTail->next;
        }

        $newHead = $newTail->next;
        $newTail->next = null;
        return $newHead;
    }
}
