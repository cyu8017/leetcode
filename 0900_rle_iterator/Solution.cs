// LeetCode 0900 - RLE Iterator
// https://leetcode.com/problems/rle-iterator/

public class RLEIterator {
    private readonly int[] enc;
    private int i;

    public RLEIterator(int[] encoding) {
        enc = (int[])encoding.Clone();
        i = 0;
    }

    public int Next(int n) {
        while (i < enc.Length) {
            if (enc[i] >= n) {
                enc[i] -= n;
                return enc[i + 1];
            }
            n -= enc[i];
            i += 2;
        }
        return -1;
    }
}
