<?php
// LeetCode 0707 - Design Linked List
// https://leetcode.com/problems/design-linked-list/

class MyLinkedList {
    private $dummy;
    private $size;

    function __construct() {
        $this->dummy = (object)['val' => 0, 'next' => null];
        $this->size = 0;
    }

    function get($index) {
        if ($index < 0 || $index >= $this->size) return -1;
        $node = $this->dummy->next;
        for ($i = 0; $i < $index; $i++) $node = $node->next;
        return $node->val;
    }

    function addAtHead($val) { $this->addAtIndex(0, $val); }

    function addAtTail($val) { $this->addAtIndex($this->size, $val); }

    function addAtIndex($index, $val) {
        if ($index < 0 || $index > $this->size) return;
        $prev = $this->dummy;
        for ($i = 0; $i < $index; $i++) $prev = $prev->next;
        $node = (object)['val' => $val, 'next' => $prev->next];
        $prev->next = $node;
        $this->size++;
    }

    function deleteAtIndex($index) {
        if ($index < 0 || $index >= $this->size) return;
        $prev = $this->dummy;
        for ($i = 0; $i < $index; $i++) $prev = $prev->next;
        $prev->next = $prev->next->next;
        $this->size--;
    }
}
