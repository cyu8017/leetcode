<?php
// LeetCode 3132 - Find the Integer Added to Array II
// https://leetcode.com/problems/find-the-integer-added-to-array-ii/

class Solution {
    public $nums1;
    public $nums2;
    function minimumAddedInteger($nums1, $nums2) {
        sort($nums1);
        sort($nums2);
        $this->nums1 = $nums1;
        $this->nums2 = $nums2;
        $ans = 1 << 30;
        for ($t = 0; $t < 3; $t++) {
            $x = $nums2[0] - $nums1[$t];
            if ($this->ok($x)) $ans = min($ans, $x);
        }
        return $ans;
    }
    function ok($x) {
        $i = 0;
        $j = 0;
        $cnt = 0;
        $n1 = count($this->nums1);
        $n2 = count($this->nums2);
        while ($i < $n1 && $j < $n2) {
            if ($this->nums2[$j] - $this->nums1[$i] !== $x) $cnt++;
            else $j++;
            $i++;
        }
        return $cnt <= 2;
    }
}
