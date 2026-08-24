<?php
// LeetCode 0347 - Top K Frequent Elements
// https://leetcode.com/problems/top-k-frequent-elements/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer[]
     */
    function topKFrequent($nums, $k) {
        return $this->top_k_frequent($nums, $k);
    }

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer[]
     */
    function top_k_frequent($nums, $k) {
        $counts = [];
        foreach ($nums as $num) {
            if (!array_key_exists($num, $counts)) {
                $counts[$num] = 0;
            }
            $counts[$num]++;
        }

        $buckets = array_fill(0, count($nums) + 1, []);
        foreach ($counts as $value => $count) {
            $buckets[$count][] = $value;
        }

        $result = [];
        for ($index = count($buckets) - 1; $index >= 0; $index--) {
            foreach ($buckets[$index] as $value) {
                $result[] = $value;
                if (count($result) === $k) {
                    return $result;
                }
            }
        }

        return $result;
    }
}
