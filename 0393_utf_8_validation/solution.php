// LeetCode 0393 - UTF-8 Validation
// https://leetcode.com/problems/utf-8-validation/

class Solution {
    /**
     * @param Integer[] $data
     * @return Boolean
     */
    function validUtf8($data) {
        return $this->valid_utf8($data);
    }

    /**
     * @param Integer[] $data
     * @return Boolean
     */
    function valid_utf8($data) {
        $remaining = 0;

        foreach ($data as $byte) {
            $byte &= 0xFF;
            if ($remaining === 0) {
                if ($byte >> 7 === 0b0) {
                    continue;
                }
                if ($byte >> 5 === 0b110) {
                    $remaining = 1;
                } elseif ($byte >> 4 === 0b1110) {
                    $remaining = 2;
                } elseif ($byte >> 3 === 0b11110) {
                    $remaining = 3;
                } else {
                    return false;
                }
            } elseif ($byte >> 6 !== 0b10) {
                return false;
            } else {
                $remaining--;
            }
        }

        return $remaining === 0;
    }
}
