// LeetCode 0468 - Validate IP Address
// https://leetcode.com/problems/validate-ip-address/

using System.Linq;

public class Solution {
    public string ValidIPAddress(string queryIP) {
        if (IsIpv4(queryIP)) {
            return "IPv4";
        }
        if (IsIpv6(queryIP)) {
            return "IPv6";
        }
        return "Neither";
    }

    private static bool IsIpv4(string address) {
        string[] parts = address.Split('.');
        if (parts.Length != 4) {
            return false;
        }
        foreach (string part in parts) {
            if (!part.All(char.IsDigit) || part.Length > 1 && part[0] == '0') {
                return false;
            }
            if (part.Length == 0 || part.Length > 3) {
                return false;
            }
            int value = int.Parse(part);
            if (value > 255) {
                return false;
            }
        }
        return true;
    }

    private static bool IsIpv6(string address) {
        string[] parts = address.Split(':');
        if (parts.Length != 8) {
            return false;
        }
        foreach (string part in parts) {
            if (part.Length == 0 || part.Length > 4) {
                return false;
            }
            if (!part.All(ch => char.IsDigit(ch) || (ch >= 'a' && ch <= 'f') || (ch >= 'A' && ch <= 'F'))) {
                return false;
            }
        }
        return true;
    }
}
