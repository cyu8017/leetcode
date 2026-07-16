// LeetCode 0093 - Restore IP Addresses
// https://leetcode.com/problems/restore-ip-addresses/

class Solution {
    /**
     * @param String $s
     * @return String[]
     */
    function restoreIpAddresses($s) {
        $result = [];
        $path = [];

        $backtrack = function ($start) use (&$s, &$result, &$path, &$backtrack) {
            if (count($path) === 4) {
                if ($start === strlen($s)) {
                    $result[] = implode('.', $path);
                }
                return;
            }

            for ($length = 1; $length <= 3; $length++) {
                if ($start + $length > strlen($s)) {
                    break;
                }
                $part = substr($s, $start, $length);
                if (($part[0] === '0' && strlen($part) > 1) || intval($part) > 255) {
                    continue;
                }
                $path[] = $part;
                $backtrack($start + $length);
                array_pop($path);
            }
        };

        $backtrack(0);
        return $result;
    }
}
