<?php
// LeetCode 1019 - Next Greater Node In Linked List
// https://leetcode.com/problems/next-greater-node-in-linked-list/

class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    /**
     * @param ListNode $head
     * @return Integer[]
     */
    function nextLargerNodes($head) {
        $vals = [];
        while ($head !== null) {
            $vals[] = $head->val;
            $head = $head->next;
        }
        $n = count($vals);
        $ans = array_fill(0, $n, 0);
        $stack = [];
        for ($i = 0; $i < $n; $i++) {
            while (!empty($stack) && $vals[end($stack)] < $vals[$i]) {
                $ans[array_pop($stack)] = $vals[$i];
            }
            $stack[] = $i;
        }
        return $ans;
    }
}
