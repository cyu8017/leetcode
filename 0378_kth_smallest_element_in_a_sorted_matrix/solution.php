// LeetCode 0378 - Kth Smallest Element in a Sorted Matrix
// https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

class Solution {
    /**
     * @param Integer[][] $matrix
     * @param Integer $k
     * @return Integer
     */
    function kthSmallest($matrix, $k) {
        return $this->kth_smallest($matrix, $k);
    }

    /**
     * @param Integer[][] $matrix
     * @param Integer $k
     * @return Integer
     */
    function kth_smallest($matrix, $k) {
        $rows = count($matrix);
        $left = $matrix[0][0];
        $right = $matrix[$rows - 1][$rows - 1];

        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            $count = 0;
            $column = $rows - 1;

            for ($row = 0; $row < $rows; $row++) {
                while ($column >= 0 && $matrix[$row][$column] > $mid) {
                    $column--;
                }
                $count += $column + 1;
            }

            if ($count < $k) {
                $left = $mid + 1;
            } else {
                $right = $mid;
            }
        }

        return $left;
    }
}
