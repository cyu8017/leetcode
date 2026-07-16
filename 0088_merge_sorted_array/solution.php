// LeetCode 0088 - Merge Sorted Array
// https://leetcode.com/problems/merge-sorted-array/

class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer $m
     * @param Integer[] $nums2
     * @param Integer $n
     * @return NULL
     */
    function merge(&$nums1, $m, $nums2, $n) {
        $i = $m - 1;
        $j = $n - 1;
        $write = $m + $n - 1;

        while ($j >= 0) {
            if ($i >= 0 && $nums1[$i] > $nums2[$j]) {
                $nums1[$write] = $nums1[$i];
                $i--;
            } else {
                $nums1[$write] = $nums2[$j];
                $j--;
            }
            $write--;
        }
    }
}
