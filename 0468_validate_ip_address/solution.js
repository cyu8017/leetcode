// LeetCode 0468 - Validate IP Address
// https://leetcode.com/problems/validate-ip-address/

class Solution {
    validIPAddress(queryIP) {
        if (this._isIpv4(queryIP)) return "IPv4";
        if (this._isIpv6(queryIP)) return "IPv6";
        return "Neither";
    }

    _isIpv4(address) {
        const parts = address.split(".");
        if (parts.length !== 4) return false;
        for (const part of parts) {
            if (!/^\d+$/.test(part) || (part.length > 1 && part[0] === "0")) return false;
            if (part.length === 0 || part.length > 3) return false;
            const value = Number(part);
            if (value > 255) return false;
        }
        return true;
    }

    _isIpv6(address) {
        const parts = address.split(":");
        if (parts.length !== 8) return false;
        const hexDigits = new Set("0123456789abcdefABCDEF".split(""));
        for (const part of parts) {
            if (!part || part.length > 4) return false;
            for (const char of part) {
                if (!hexDigits.has(char)) return false;
            }
        }
        return true;
    }
}

module.exports = { Solution };
