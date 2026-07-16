// LeetCode 0249 - Group Shifted Strings
// https://leetcode.com/problems/group-shifted-strings/

class Solution {
    /**
     * @param String[] $strings
     * @return String[][]
     */
    function groupStrings($strings) {
        $groups = [];
        foreach ($strings as $text) {
            if ($text === "") {
                $key = "";
            } else {
                $base = ord($text[0]);
                $shifts = [];
                for ($index = 0; $index < strlen($text); $index++) {
                    $shifts[] = (ord($text[$index]) - $base + 26) % 26;
                }
                $key = implode(",", $shifts);
            }
            if (!array_key_exists($key, $groups)) {
                $groups[$key] = [];
            }
            $groups[$key][] = $text;
        }
        return array_values($groups);
    }
}
