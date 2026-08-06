<?php
class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function widestPairOfIndices($nums1, $nums2) {
        $first = [0 => -1];
        $ans = 0;
        $s = 0;
        $m = count($nums1);
        for ($i = 0; $i < $m; $i++) {
            $s += $nums1[$i] - $nums2[$i];
            if (array_key_exists($s, $first)) {
                $ans = max($ans, $i - $first[$s]);
            } else {
                $first[$s] = $i;
            }
        }
        return $ans;
    }
}
