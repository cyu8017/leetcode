// LeetCode 0259 - 3Sum Smaller
// https://leetcode.com/problems/3sum-smaller/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function threeSumSmaller($nums, $target) {
        sort($nums);
        $count = 0;
        $length = count($nums);
        for ($index = 0; $index < $length - 2; $index++) {
            $left = $index + 1;
            $right = $length - 1;
            while ($left < $right) {
                $total = $nums[$index] + $nums[$left] + $nums[$right];
                if ($total < $target) {
                    $count += $right - $left;
                    $left++;
                } else {
                    $right--;
                }
            }
        }
        return $count;
    }
}
