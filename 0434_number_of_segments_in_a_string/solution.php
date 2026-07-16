// LeetCode 0434 - Number of Segments in a String
// https://leetcode.com/problems/number-of-segments-in-a-string/

class Solution {
    /**
     * @param string $s
     * @return int
     */
    function countSegments($s) {
        return $this->count_segments($s);
    }

    /**
     * @param string $s
     * @return int
     */
    function count_segments($s) {
        $count = 0;
        $inSegment = false;
        $length = strlen($s);
        for ($index = 0; $index < $length; $index++) {
            if ($s[$index] !== " ") {
                if (!$inSegment) {
                    $count++;
                    $inSegment = true;
                }
            } else {
                $inSegment = false;
            }
        }
        return $count;
    }
}
