// LeetCode 0751 - IP to CIDR
// https://leetcode.com/problems/ip-to-cidr/

import java.util.*;

class Solution {
    public List<String> ipToCIDR(String ip, int n) {
        long start = ipToInt(ip);
        List<String> answer = new ArrayList<>();
        while (n > 0) {
            long lowbit = start == 0 ? (1L << 32) : (start & -start);
            while (lowbit > n) lowbit >>= 1;
            int mask = 32 - (bitLength(lowbit) - 1);
            answer.add(intToIp(start) + "/" + mask);
            start += lowbit;
            n -= (int) lowbit;
        }
        return answer;
    }

    private long ipToInt(String value) {
        long result = 0;
        for (String part : value.split("\\.")) result = result * 256 + Long.parseLong(part);
        return result;
    }

    private String intToIp(long value) {
        return ((value >> 24) & 255) + "." + ((value >> 16) & 255) + "." + ((value >> 8) & 255) + "." + (value & 255);
    }

    private int bitLength(long value) {
        int len = 0;
        while (value > 0) { value >>= 1; len++; }
        return len;
    }
}
