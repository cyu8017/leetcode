// LeetCode 0264 - Ugly Number II
// https://leetcode.com/problems/ugly-number-ii/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function nthUglyNumber($n) {
        $ugly = [1];
        $index2 = 0;
        $index3 = 0;
        $index5 = 0;
        while (count($ugly) < $n) {
            $nextUgly = min($ugly[$index2] * 2, $ugly[$index3] * 3, $ugly[$index5] * 5);
            $ugly[] = $nextUgly;
            if ($nextUgly === $ugly[$index2] * 2) {
                $index2++;
            }
            if ($nextUgly === $ugly[$index3] * 3) {
                $index3++;
            }
            if ($nextUgly === $ugly[$index5] * 5) {
                $index5++;
            }
        }
        return $ugly[count($ugly) - 1];
    }
}
