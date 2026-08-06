<?php
// LeetCode 1265 - Print Immutable Linked List in Reverse
// https://leetcode.com/problems/print-immutable-linked-list-in-reverse/

class Solution {
    /**
     * @param ImmutableListNode $head
     * @return NULL
     */
    function printLinkedListInReverse($head) {
        if ($head === null) return;
        $this->printLinkedListInReverse($head->getNext());
        $head->printValue();
    }
}
