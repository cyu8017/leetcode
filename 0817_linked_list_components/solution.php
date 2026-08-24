<?php
// LeetCode 0817 - Linked List Components
// https://leetcode.com/problems/linked-list-components/

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
     * @param Integer[] $nums
     * @return Integer
     */
    function numComponents($head, $nums) {
        $present = [];
        foreach ($nums as $x) $present[$x] = true;
        $count = 0;
        $connected = false;
        while ($head !== null) {
            if (isset($present[$head->val])) {
                if (!$connected) {
                    $count++;
                    $connected = true;
                }
            } else {
                $connected = false;
            }
            $head = $head->next;
        }
        return $count;
    }
}
