<?php
// LeetCode 1290 - Convert Binary Number in a Linked List to Integer
// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

class Solution {
    /**
     * @param ListNode $head
     * @return Integer
     */
    function getDecimalValue($head) {
        $value = 0;
        while ($head !== null) {
            $value = $value * 2 + $head->val;
            $head = $head->next;
        }
        return $value;
    }
}
