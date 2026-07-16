// LeetCode 0401 - Binary Watch
// https://leetcode.com/problems/binary-watch/

class Solution {
    /**
     * @param Integer $turnedOn
     * @return String[]
     */
    function readBinaryWatch($turnedOn) {
        return $this->read_binary_watch($turnedOn);
    }

    /**
     * @param Integer $turnedOn
     * @return String[]
     */
    function read_binary_watch($turnedOn) {
        $result = [];
        for ($hour = 0; $hour < 12; $hour++) {
            for ($minute = 0; $minute < 60; $minute++) {
                if (substr_count(decbin($hour), "1") + substr_count(decbin($minute), "1") === $turnedOn) {
                    $result[] = sprintf("%d:%02d", $hour, $minute);
                }
            }
        }
        return $result;
    }
}
