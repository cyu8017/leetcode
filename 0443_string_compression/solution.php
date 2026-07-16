// LeetCode 0443 - String Compression
// https://leetcode.com/problems/string-compression/

class Solution {
    /**
     * @param String[] $chars
     * @return int
     */
    function compress(&$chars) {
        $write = 0;
        $read = 0;
        $length = count($chars);
        while ($read < $length) {
            $char = $chars[$read];
            $count = 0;
            while ($read < $length && $chars[$read] === $char) {
                $read++;
                $count++;
            }
            $chars[$write] = $char;
            $write++;
            if ($count > 1) {
                foreach (str_split((string)$count) as $digit) {
                    $chars[$write] = $digit;
                    $write++;
                }
            }
        }
        return $write;
    }
}
