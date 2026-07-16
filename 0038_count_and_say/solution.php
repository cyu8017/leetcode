// LeetCode 0038 - Count and Say
// https://leetcode.com/problems/count-and-say/

class Solution {
    /**
     * @param Integer $n
     * @return String
     */
    function countAndSay($n) {
        $term = "1";

        for ($i = 1; $i < $n; $i++) {
            $nextTerm = [];
            $index = 0;
            $length = strlen($term);
            while ($index < $length) {
                $count = 1;
                while ($index + $count < $length && $term[$index + $count] === $term[$index]) {
                    $count++;
                }
                $nextTerm[] = (string) $count;
                $nextTerm[] = $term[$index];
                $index += $count;
            }
            $term = implode('', $nextTerm);
        }

        return $term;
    }
}
