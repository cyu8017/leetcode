<?php
// LeetCode 2058 - Find the Minimum and Maximum Number of Nodes Between Critical Points
// https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

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
    function nodesBetweenCriticalPoints($head) {
        $crit = [];
        $prev = $head;
        $cur = $head->next;
        $idx = 1;
        while ($cur && $cur->next) {
            if (($cur->val > $prev->val && $cur->val > $cur->next->val) ||
                ($cur->val < $prev->val && $cur->val < $cur->next->val))
                $crit[] = $idx;
            $prev = $cur;
            $cur = $cur->next;
            $idx++;
        }
        if (count($crit) < 2) return [-1, -1];
        $mn = $crit[1] - $crit[0];
        $cn = count($crit);
        for ($i = 2; $i < $cn; $i++) $mn = min($mn, $crit[$i] - $crit[$i - 1]);
        return [$mn, $crit[$cn - 1] - $crit[0]];
    }
}
