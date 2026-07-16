// LeetCode 0271 - Encode and Decode Strings
// https://leetcode.com/problems/encode-and-decode-strings/

class Codec {
    /**
     * @param String[] $strs
     * @return String
     */
    function encode($strs) {
        $encoded = "";
        foreach ($strs as $text) {
            $encoded .= strlen($text) . "#" . $text;
        }
        return $encoded;
    }

    /**
     * @param String $encoded
     * @return String[]
     */
    function decode($encoded) {
        $result = [];
        $index = 0;
        $length = strlen($encoded);
        while ($index < $length) {
            $delimiter = strpos($encoded, "#", $index);
            $chunk = (int)substr($encoded, $index, $delimiter - $index);
            $start = $delimiter + 1;
            $result[] = substr($encoded, $start, $chunk);
            $index = $start + $chunk;
        }
        return $result;
    }
}
