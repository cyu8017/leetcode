<?php
// LeetCode 0328 - Odd Even Linked List
// https://leetcode.com/problems/odd-even-linked-list/

class ListNode {
    public $val;
    public $next;

    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    /**
     * @param ListNode|null $head
     * @return ListNode|null
     */
    function oddEvenList($head) {
        if ($head === null || $head->next === null) {
            return $head;
        }

        $odd = $head;
        $even = $head->next;
        $evenHead = $even;
        while ($even !== null && $even->next !== null) {
            $odd->next = $even->next;
            $odd = $odd->next;
            $even->next = $odd->next;
            $even = $even->next;
        }
        $odd->next = $evenHead;
        return $head;
    }
}
