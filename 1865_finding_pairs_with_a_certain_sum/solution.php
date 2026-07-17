<?php
// LeetCode 1865 - Finding Pairs With a Certain Sum
// https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

class FindSumPairs {
    /** @var Integer[] */
    private $nums1;
    /** @var Integer[] */
    private $nums2;
    /** @var array<int, int> */
    private $counts;

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     */
    function __construct($nums1, $nums2) {
        $this->nums1 = $nums1;
        $this->nums2 = $nums2;
        $this->counts = [];
        foreach ($nums2 as $num) {
            if (!isset($this->counts[$num])) {
                $this->counts[$num] = 0;
            }
            $this->counts[$num]++;
        }
    }

    /**
     * @param Integer $index
     * @param Integer $val
     * @return void
     */
    function add($index, $val) {
        $old = $this->nums2[$index];
        $this->counts[$old]--;
        $this->nums2[$index] += $val;
        $new = $this->nums2[$index];
        if (!isset($this->counts[$new])) {
            $this->counts[$new] = 0;
        }
        $this->counts[$new]++;
    }

    /**
     * @param Integer $tot
     * @return Integer
     */
    function count($tot) {
        $result = 0;
        foreach ($this->nums1 as $num) {
            $need = $tot - $num;
            if (isset($this->counts[$need])) {
                $result += $this->counts[$need];
            }
        }
        return $result;
    }
}
