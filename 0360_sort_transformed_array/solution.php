// LeetCode 0360 - Sort Transformed Array
// https://leetcode.com/problems/sort-transformed-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $a
     * @param Integer $b
     * @param Integer $c
     * @return Integer[]
     */
    function sortTransformedArray($nums, $a, $b, $c) {
        return $this->sort_transformed_array($nums, $a, $b, $c);
    }

    /**
     * @param Integer[] $nums
     * @param Integer $a
     * @param Integer $b
     * @param Integer $c
     * @return Integer[]
     */
    function sort_transformed_array($nums, $a, $b, $c) {
        $transform = function ($value) use ($a, $b, $c) {
            return $a * $value * $value + $b * $value + $c;
        };

        $left = 0;
        $right = count($nums) - 1;
        $result = array_fill(0, count($nums), 0);
        $index = $a > 0 ? count($nums) - 1 : 0;
        $step = $a > 0 ? -1 : 1;

        while ($left <= $right) {
            $leftValue = $transform($nums[$left]);
            $rightValue = $transform($nums[$right]);

            if ($a > 0) {
                if ($leftValue > $rightValue) {
                    $result[$index] = $leftValue;
                    $left++;
                } else {
                    $result[$index] = $rightValue;
                    $right--;
                }
            } elseif ($leftValue < $rightValue) {
                $result[$index] = $leftValue;
                $left++;
            } else {
                $result[$index] = $rightValue;
                $right--;
            }

            $index += $step;
        }

        return $result;
    }
}
