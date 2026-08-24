<?php
// LeetCode 0708 - Insert into a Sorted Circular Linked List
// https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

class Node {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    function insert($head, $insertVal) {
        $node = new Node($insertVal);
        if ($head === null) {
            $node->next = $node;
            return $node;
        }
        $cur = $head;
        while ($cur->next !== null && $cur->next !== $head) $cur = $cur->next;
        $cur->next = $head;
        $prev = $head;
        $curr = $head->next;
        while (true) {
            if ($prev->val <= $insertVal && $insertVal <= $curr->val) break;
            if ($prev->val > $curr->val && ($insertVal >= $prev->val || $insertVal <= $curr->val)) break;
            $prev = $curr;
            $curr = $curr->next;
            if ($prev === $head) break;
        }
        $prev->next = $node;
        $node->next = $curr;
        return $head;
    }
}
