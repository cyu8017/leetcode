// LeetCode 0751 - IP to CIDR
// https://leetcode.com/problems/ip-to-cidr/

using System.Collections.Generic;

public class Solution {
    public IList<string> IpToCIDR(string ip, int n) {
        long start = IpToInt(ip);
        var answer = new List<string>();
        while (n > 0) {
            long lowbit = start == 0 ? (1L << 32) : (start & -start);
            while (lowbit > n) lowbit >>= 1;
            int mask = 32 - (BitLength(lowbit) - 1);
            answer.Add(IntToIp(start) + "/" + mask);
            start += lowbit;
            n -= (int)lowbit;
        }
        return answer;
    }

    private long IpToInt(string value) {
        long result = 0;
        foreach (string part in value.Split('.')) result = result * 256 + long.Parse(part);
        return result;
    }

    private string IntToIp(long value) =>
        ((value >> 24) & 255) + "." + ((value >> 16) & 255) + "." + ((value >> 8) & 255) + "." + (value & 255);

    private int BitLength(long value) {
        int len = 0;
        while (value > 0) { value >>= 1; len++; }
        return len;
    }
}
