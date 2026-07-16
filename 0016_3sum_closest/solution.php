// LeetCode 0016 - 3Sum Closest
// https://leetcode.com/problems/3sum-closest/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function threeSumClosest($nums, $target) {
        sort($nums);
        $closest = $nums[0] + $nums[1] + $nums[2];
        $n = count($nums);

        for ($i = 0; $i < $n - 2; $i++) {
            $left = $i + 1;
            $right = $n - 1;
            while ($left < $right) {
                $total = $nums[$i] + $nums[$left] + $nums[$right];
                if (abs($total - $target) < abs($closest - $target)) {
                    $closest = $total;
                }
                if ($total < $target) {
                    $left++;
                } elseif ($total > $target) {
                    $right--;
                } else {
                    return $total;
                }
            }
        }

        return $closest;
    }
}
