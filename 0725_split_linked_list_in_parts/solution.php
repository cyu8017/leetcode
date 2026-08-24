<?php
// LeetCode 0725 - Split Linked List in Parts
// https://leetcode.com/problems/split-linked-list-in-parts/

class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    function splitListToParts($head, $k) {
        $length = 0;
        for ($node = $head; $node !== null; $node = $node->next) $length++;
        $partSize = intdiv($length, $k);
        $extra = $length % $k;
        $result = array_fill(0, $k, null);
        $current = $head;
        for ($i = 0; $i < $k; $i++) {
            $result[$i] = $current;
            $size = $partSize + ($i < $extra ? 1 : 0);
            for ($j = 0; $j < $size - 1 && $current !== null; $j++) $current = $current->next;
            if ($current !== null) {
                $nxt = $current->next;
                $current->next = null;
                $current = $nxt;
            }
        }
        return $result;
    }
}
