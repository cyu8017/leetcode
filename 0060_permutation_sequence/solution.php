// LeetCode 0060 - Permutation Sequence
// https://leetcode.com/problems/permutation-sequence/

class Solution {
    /**
     * @param Integer $n
     * @param Integer $k
     * @return String
     */
    function getPermutation($n, $k) {
        $numbers = range(1, $n);
        $factorials = array_fill(0, $n, 1);

        for ($i = 1; $i < $n; $i++) {
            $factorials[$i] = $factorials[$i - 1] * $i;
        }

        $k--;
        $result = '';

        for ($i = $n - 1; $i >= 0; $i--) {
            $index = intdiv($k, $factorials[$i]);
            $result .= (string)$numbers[$index];
            array_splice($numbers, $index, 1);
            $k %= $factorials[$i];
        }

        return $result;
    }
}
