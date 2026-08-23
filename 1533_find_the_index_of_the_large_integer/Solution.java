// LeetCode 1533 - Find the Index of the Large Integer
// https://leetcode.com/problems/find-the-index-of-the-large-integer/

class ArrayReader {
    private final int[] arr;

    ArrayReader(int[] arr) {
        this.arr = arr;
    }

    public int compareSub(int l, int r, int x, int y) {
        long a = 0;
        long b = 0;
        for (int i = l; i <= r; i++) {
            a += arr[i];
        }
        for (int i = x; i <= y; i++) {
            b += arr[i];
        }
        return Long.compare(a, b);
    }

    public int length() {
        return arr.length;
    }
}

class Solution {
    public int getIndex(int[] arr) {
        return getIndex(new ArrayReader(arr));
    }

    public int getIndex(ArrayReader reader) {
        int left = 0;
        int right = reader.length() - 1;
        while (left < right) {
            int length = right - left + 1;
            int half = length / 2;
            int result = reader.compareSub(left, left + half - 1, right - half + 1, right);
            if (result == 0) {
                return left + half;
            }
            if (result > 0) {
                right = left + half - 1;
            } else {
                left = right - half + 1;
            }
        }
        return left;
    }
}
