<?php
// LeetCode 0295 - Find Median from Data Stream
// https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder {
    /** @var int[] */
    private $small;
    /** @var int[] */
    private $large;

    function __construct() {
        $this->small = [];
        $this->large = [];
    }

    /**
     * @param Integer $num
     * @return void
     */
    function addNum($num) {
        $this->push($this->small, -$num, true);
        $this->push($this->large, -$this->pop($this->small, true), false);
        if (count($this->large) > count($this->small)) {
            $this->push($this->small, -$this->pop($this->large, false), true);
        }
    }

    /**
     * @return Float
     */
    function findMedian() {
        if (count($this->small) > count($this->large)) {
            return (float)(-$this->small[0]);
        }
        return (-$this->small[0] + $this->large[0]) / 2.0;
    }

    /**
     * @param int[] $heap
     * @param int $value
     * @param bool $isMaxHeap
     * @return void
     */
    private function push(&$heap, $value, $isMaxHeap) {
        $heap[] = $value;
        $this->bubbleUp($heap, count($heap) - 1, $isMaxHeap);
    }

    /**
     * @param int[] $heap
     * @param bool $isMaxHeap
     * @return int
     */
    private function pop(&$heap, $isMaxHeap) {
        $top = $heap[0];
        $last = array_pop($heap);
        if (count($heap) > 0) {
            $heap[0] = $last;
            $this->bubbleDown($heap, 0, $isMaxHeap);
        }
        return $top;
    }

    /**
     * @param int[] $heap
     * @param int $index
     * @param bool $isMaxHeap
     * @return void
     */
    private function bubbleUp(&$heap, $index, $isMaxHeap) {
        while ($index > 0) {
            $parent = intdiv($index - 1, 2);
            if ($isMaxHeap ? $heap[$index] <= $heap[$parent] : $heap[$index] >= $heap[$parent]) {
                break;
            }
            $tmp = $heap[$index];
            $heap[$index] = $heap[$parent];
            $heap[$parent] = $tmp;
            $index = $parent;
        }
    }

    /**
     * @param int[] $heap
     * @param int $index
     * @param bool $isMaxHeap
     * @return void
     */
    private function bubbleDown(&$heap, $index, $isMaxHeap) {
        while (true) {
            $target = $index;
            $left = $index * 2 + 1;
            $right = $left + 1;
            if ($left < count($heap) && ($isMaxHeap ? $heap[$left] > $heap[$target] : $heap[$left] < $heap[$target])) {
                $target = $left;
            }
            if ($right < count($heap) && ($isMaxHeap ? $heap[$right] > $heap[$target] : $heap[$right] < $heap[$target])) {
                $target = $right;
            }
            if ($target === $index) {
                break;
            }
            $tmp = $heap[$index];
            $heap[$index] = $heap[$target];
            $heap[$target] = $tmp;
            $index = $target;
        }
    }
}
