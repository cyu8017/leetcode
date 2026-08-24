<?php
// LeetCode 2336 - Smallest Number in Infinite Set
// https://leetcode.com/problems/smallest-number-in-infinite-set/

class SmallestInfiniteSet {
    private $next;
    private $added;
    private $heap;

    function __construct() {
        $this->next = 1;
        $this->added = [];
        $this->heap = new SplPriorityQueue();
        $this->heap->setExtractFlags(SplPriorityQueue::EXTR_DATA);
    }

    function popSmallest() {
        if (!$this->heap->isEmpty()) {
            $x = $this->heap->extract();
            unset($this->added[$x]);
            return $x;
        }
        return $this->next++;
    }

    function addBack($num) {
        if ($num < $this->next && !isset($this->added[$num])) {
            $this->added[$num] = true;
            $this->heap->insert($num, -$num);
        }
    }
}
