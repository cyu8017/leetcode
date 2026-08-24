<?php
// LeetCode 2807 - Insert Greatest Common Divisors in Linked List
// https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    function insertGreatestCommonDivisors($head) {
        $gcd = function($a, $b) {
            while ($b) { $t = $a % $b; $a = $b; $b = $t; }
            return $a;
        };
        $cur = $head;
        while ($cur && $cur->next) {
            $g = $gcd($cur->val, $cur->next->val);
            $node = new ListNode($g, $cur->next);
            $cur->next = $node;
            $cur = $node->next;
        }
        return $head;
    }
}
