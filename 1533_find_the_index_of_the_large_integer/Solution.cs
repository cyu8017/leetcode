// LeetCode 1533 - Find the Index of the Large Integer
// https://leetcode.com/problems/find-the-index-of-the-large-integer/

using System.Linq;

public class ArrayReader {
    private readonly int[] arr;
    public ArrayReader(int[] arr) { this.arr = arr; }
    public int CompareSub(int l, int r, int x, int y) {
        long a = 0, b = 0;
        for (int i = l; i <= r; i++) a += arr[i];
        for (int i = x; i <= y; i++) b += arr[i];
        return a.CompareTo(b);
    }
    public int Length() => arr.Length;
}

public class Solution {
    public int GetIndex(int[] arr) => GetIndex(new ArrayReader(arr));

    public int GetIndex(ArrayReader reader) {
        int left = 0, right = reader.Length() - 1;
        while (left < right) {
            int length = right - left + 1;
            int half = length / 2;
            int result = reader.CompareSub(left, left + half - 1, right - half + 1, right);
            if (result == 0) return left + half;
            if (result > 0) right = left + half - 1;
            else left = right - half + 1;
        }
        return left;
    }
}
