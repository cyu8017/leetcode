// LeetCode 0468 - Validate IP Address
// https://leetcode.com/problems/validate-ip-address/

class Solution {
    public String validIPAddress(String queryIP) {
        if (isIpv4(queryIP)) {
            return "IPv4";
        }
        if (isIpv6(queryIP)) {
            return "IPv6";
        }
        return "Neither";
    }

    private boolean isIpv4(String address) {
        String[] parts = address.split("\\.", -1);
        if (parts.length != 4) {
            return false;
        }
        for (String part : parts) {
            if (!part.matches("\\d+") || part.length() > 1 && part.charAt(0) == '0') {
                return false;
            }
            if (part.isEmpty() || part.length() > 3) {
                return false;
            }
            int value = Integer.parseInt(part);
            if (value > 255) {
                return false;
            }
        }
        return true;
    }

    private boolean isIpv6(String address) {
        String[] parts = address.split(":", -1);
        if (parts.length != 8) {
            return false;
        }
        for (String part : parts) {
            if (part.isEmpty() || part.length() > 4) {
                return false;
            }
            for (int index = 0; index < part.length(); index++) {
                char ch = part.charAt(index);
                boolean isDigit = ch >= '0' && ch <= '9';
                boolean isLower = ch >= 'a' && ch <= 'f';
                boolean isUpper = ch >= 'A' && ch <= 'F';
                if (!isDigit && !isLower && !isUpper) {
                    return false;
                }
            }
        }
        return true;
    }
}
