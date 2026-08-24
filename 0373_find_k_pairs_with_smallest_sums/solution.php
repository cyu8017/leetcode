<?php
// LeetCode 0373 - Find K Pairs with Smallest Sums
// https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer $k
     * @return Integer[][]
     */
    function kSmallestPairs($nums1, $nums2, $k) {
        return $this->k_smallest_pairs($nums1, $nums2, $k);
    }

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer $k
     * @return Integer[][]
     */
    function k_smallest_pairs($nums1, $nums2, $k) {
        if (count($nums1) === 0 || count($nums2) === 0 || $k === 0) {
            return [];
        }

        $heap = [];
        $limit = min(count($nums1), $k);
        for ($index = 0; $index < $limit; $index++) {
            $this->heapPush($heap, [$nums1[$index] + $nums2[0], $index, 0]);
        }

        $result = [];
        while (count($heap) > 0 && count($result) < $k) {
            [, $index1, $index2] = $this->heapPop($heap);
            $result[] = [$nums1[$index1], $nums2[$index2]];
            if ($index2 + 1 < count($nums2)) {
                $this->heapPush($heap, [$nums1[$index1] + $nums2[$index2 + 1], $index1, $index2 + 1]);
            }
        }

        return $result;
    }

    /**
     * @param array<int, array{0: int, 1: int, 2: int}> $heap
     * @param array{0: int, 1: int, 2: int} $item
     * @return void
     */
    private function heapPush(&$heap, $item) {
        $heap[] = $item;
        $index = count($heap) - 1;
        while ($index > 0) {
            $parent = intdiv($index - 1, 2);
            if ($heap[$parent][0] <= $heap[$index][0]) {
                break;
            }
            $tmp = $heap[$index];
            $heap[$index] = $heap[$parent];
            $heap[$parent] = $tmp;
            $index = $parent;
        }
    }

    /**
     * @param array<int, array{0: int, 1: int, 2: int}> $heap
     * @return array{0: int, 1: int, 2: int}
     */
    private function heapPop(&$heap) {
        $top = $heap[0];
        $last = array_pop($heap);
        if (count($heap) === 0) {
            return $top;
        }
        $heap[0] = $last;
        $index = 0;
        while (true) {
            $smallest = $index;
            $left = $index * 2 + 1;
            $right = $index * 2 + 2;
            if ($left < count($heap) && $heap[$left][0] < $heap[$smallest][0]) {
                $smallest = $left;
            }
            if ($right < count($heap) && $heap[$right][0] < $heap[$smallest][0]) {
                $smallest = $right;
            }
            if ($smallest === $index) {
                break;
            }
            $tmp = $heap[$index];
            $heap[$index] = $heap[$smallest];
            $heap[$smallest] = $tmp;
            $index = $smallest;
        }
        return $top;
    }
}
