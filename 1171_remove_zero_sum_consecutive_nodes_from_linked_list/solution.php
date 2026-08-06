<?php
// LeetCode 1171 - Remove Zero Sum Consecutive Nodes from Linked List
// https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

class Solution {
    /**
     * @param ListNode $head
     * @return ListNode
     */
    function removeZeroSumSublists($head) {
        $dummy = (object)['val' => 0, 'next' => $head];
        $prefix = 0;
        $seen = [0 => $dummy];
        $node = $dummy;
        while ($node !== null) {
            $prefix += $node->val;
            $seen[$prefix] = $node;
            $node = $node->next;
        }
        $prefix = 0;
        $node = $dummy;
        while ($node !== null) {
            $prefix += $node->val;
            $node->next = $seen[$prefix]->next;
            $node = $node->next;
        }
        return $dummy->next;
    }
}
