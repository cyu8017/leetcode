// LeetCode 0900 - RLE Iterator
// https://leetcode.com/problems/rle-iterator/

class RLEIterator {
    private final int[] enc;
    private int i;

    public RLEIterator(int[] encoding) {
        enc = encoding.clone();
        i = 0;
    }

    public int next(int n) {
        while (i < enc.length) {
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
