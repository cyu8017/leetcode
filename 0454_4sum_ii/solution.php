// LeetCode 0454 - 4Sum II
// https://leetcode.com/problems/4sum-ii/

class Solution {
    /**
     * @param int[] $nums1
     * @param int[] $nums2
     * @param int[] $nums3
     * @param int[] $nums4
     * @return int
     */
    function fourSumCount($nums1, $nums2, $nums3, $nums4) {
        return $this->four_sum_count($nums1, $nums2, $nums3, $nums4);
    }

    /**
     * @param int[] $nums1
     * @param int[] $nums2
     * @param int[] $nums3
     * @param int[] $nums4
     * @return int
     */
    function four_sum_count($nums1, $nums2, $nums3, $nums4) {
        $pairSums = [];
        foreach ($nums1 as $a) {
            foreach ($nums2 as $b) {
                $sum = $a + $b;
                if (!array_key_exists($sum, $pairSums)) {
                    $pairSums[$sum] = 0;
                }
                $pairSums[$sum]++;
            }
        }

        $total = 0;
        foreach ($nums3 as $c) {
            foreach ($nums4 as $d) {
                $target = -($c + $d);
                if (array_key_exists($target, $pairSums)) {
                    $total += $pairSums[$target];
                }
            }
        }
        return $total;
    }
}
