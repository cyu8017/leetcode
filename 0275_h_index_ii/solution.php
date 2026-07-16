// LeetCode 0275 - H-Index II
// https://leetcode.com/problems/h-index-ii/

class Solution {
    /**
     * @param Integer[] $citations
     * @return Integer
     */
    function hIndex($citations) {
        $left = 0;
        $right = count($citations) - 1;
        $length = count($citations);
        while ($left <= $right) {
            $mid = intdiv($left + $right, 2);
            $papers = $length - $mid;
            if ($citations[$mid] >= $papers) {
                $right = $mid - 1;
            } else {
                $left = $mid + 1;
            }
        }
        return $length - $left;
    }
}
