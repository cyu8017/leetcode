// LeetCode 0034 - Find First and Last Position of Element in Sorted Array
// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function searchRange($nums, $target) {
        if (count($nums) === 0) {
            return [-1, -1];
        }

        $start = $this->lowerBound($nums, $target);
        if ($start === count($nums) || $nums[$start] !== $target) {
            return [-1, -1];
        }

        return [$start, $this->upperBound($nums, $target) - 1];
    }

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    private function lowerBound($nums, $target) {
        $left = 0;
        $right = count($nums);

        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            if ($nums[$mid] < $target) {
                $left = $mid + 1;
            } else {
                $right = $mid;
            }
        }

        return $left;
    }

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    private function upperBound($nums, $target) {
        $left = 0;
        $right = count($nums);

        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            if ($nums[$mid] <= $target) {
                $left = $mid + 1;
            } else {
                $right = $mid;
            }
        }

        return $left;
    }
}
