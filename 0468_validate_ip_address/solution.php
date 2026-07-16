// LeetCode 0468 - Validate IP Address
// https://leetcode.com/problems/validate-ip-address/

class Solution {
    /**
     * @param string $queryIP
     * @return string
     */
    function validIPAddress($queryIP) {
        return $this->valid_ip_address($queryIP);
    }

    /**
     * @param string $queryIP
     * @return string
     */
    function valid_ip_address($queryIP) {
        if ($this->isIpv4($queryIP)) {
            return 'IPv4';
        }
        if ($this->isIpv6($queryIP)) {
            return 'IPv6';
        }
        return 'Neither';
    }

    private function isIpv4(string $address): bool {
        $parts = explode('.', $address);
        if (count($parts) !== 4) {
            return false;
        }

        foreach ($parts as $part) {
            if (!ctype_digit($part) || (strlen($part) > 1 && $part[0] === '0')) {
                return false;
            }
            if ($part === '' || strlen($part) > 3) {
                return false;
            }
            if ((int)$part > 255) {
                return false;
            }
        }

        return true;
    }

    private function isIpv6(string $address): bool {
        $parts = explode(':', $address);
        if (count($parts) !== 8) {
            return false;
        }

        $hexDigits = '0123456789abcdefABCDEF';
        foreach ($parts as $part) {
            if ($part === '' || strlen($part) > 4) {
                return false;
            }
            $length = strlen($part);
            for ($index = 0; $index < $length; $index++) {
                if (strpos($hexDigits, $part[$index]) === false) {
                    return false;
                }
            }
        }

        return true;
    }
}
