// LeetCode 3199 - Count Triplets with Even XOR Set Bits I
// https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-i/

public class Solution {
    public int TripletCount(int[] a, int[] b, int[] c) {
        int[] cnt1 = new int[2], cnt2 = new int[2], cnt3 = new int[2];
        foreach (int x in a) cnt1[PopCount(x) % 2]++;
        foreach (int x in b) cnt2[PopCount(x) % 2]++;
        foreach (int x in c) cnt3[PopCount(x) % 2]++;
        int ans = 0;
        for (int i = 0; i < 2; i++)
            for (int j = 0; j < 2; j++)
                for (int k = 0; k < 2; k++)
                    if ((i + j + k) % 2 == 0) ans += cnt1[i] * cnt2[j] * cnt3[k];
        return ans;
    }

    static int PopCount(int x) {
        int c = 0;
        unchecked {
            uint u = (uint)x;
            while (u != 0) { c += (int)(u & 1); u >>= 1; }
        }
        return c;
    }
}
