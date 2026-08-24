<?php
// LeetCode 2074 - Reverse Nodes in Even Length Groups
// https://leetcode.com/problems/reverse-nodes-in-even-length-groups/

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
     * @return ListNode
     */
    function reverseEvenLengthGroups($head) {
        $dummy = new ListNode(0, $head);
        $prev = $dummy;
        $group = 1;
        while ($prev->next) {
            $cur = $prev->next;
            $cnt = 0;
            $node = $cur;
            while ($node && $cnt < $group) { $node = $node->next; $cnt++; }
            if ($cnt % 2 === 0) {
                $revPrev = $node;
                $p = $cur;
                for ($i = 0; $i < $cnt; $i++) {
                    $nxt = $p->next;
                    $p->next = $revPrev;
                    $revPrev = $p;
                    $p = $nxt;
                }
                $prev->next = $revPrev;
                $prev = $cur;
            } else {
                for ($i = 0; $i < $cnt; $i++) $prev = $prev->next;
            }
            $group++;
        }
        return $dummy->next;
    }
}
