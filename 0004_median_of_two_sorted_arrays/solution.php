// LeetCode 0004 - Median of Two Sorted Arrays
// https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Float
     */
    function findMedianSortedArrays($nums1, $nums2) {
        if (count($nums1) > count($nums2)) {
            [$nums1, $nums2] = [$nums2, $nums1];
        }

        $m = count($nums1);
        $n = count($nums2);
        $totalLeft = intdiv($m + $n + 1, 2);
        $lo = 0;
        $hi = $m;

        while ($lo <= $hi) {
            $i = intdiv($lo + $hi, 2);
            $j = $totalLeft - $i;

            $nums1LeftMax = $i === 0 ? PHP_INT_MIN : $nums1[$i - 1];
            $nums1RightMin = $i === $m ? PHP_INT_MAX : $nums1[$i];
            $nums2LeftMax = $j === 0 ? PHP_INT_MIN : $nums2[$j - 1];
            $nums2RightMin = $j === $n ? PHP_INT_MAX : $nums2[$j];

            if ($nums1LeftMax <= $nums2RightMin && $nums2LeftMax <= $nums1RightMin) {
                if (($m + $n) % 2 === 1) {
                    return (float)max($nums1LeftMax, $nums2LeftMax);
                }
                return (max($nums1LeftMax, $nums2LeftMax) + min($nums1RightMin, $nums2RightMin)) / 2.0;
            }

            if ($nums1LeftMax > $nums2RightMin) {
                $hi = $i - 1;
            } else {
                $lo = $i + 1;
            }
        }

        return 0.0;
    }
}
