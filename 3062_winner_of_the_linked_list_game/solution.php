<?php
// LeetCode 3062 - Winner of the Linked List Game
// https://leetcode.com/problems/winner-of-the-linked-list-game/

class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    function gameResult($head) {
        $odd = 0;
        $even = 0;
        for (; $head !== null; $head = $head->next->next) {
            $a = $head->val;
            $b = $head->next->val;
            if ($a < $b) $odd++;
            if ($a > $b) $even++;
        }
        if ($odd > $even) return "Odd";
        if ($odd < $even) return "Even";
        return "Tie";
    }
}
