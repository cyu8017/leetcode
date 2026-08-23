// LeetCode 0702 - Search in a Sorted Array of Unknown Size
// https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/

public class ArrayReader {
    private readonly int[] secret;
    public ArrayReader(int[] secret) { this.secret = secret; }
    public int Get(int index) {
        if (index < 0 || index >= secret.Length) return 2147483647;
        return secret[index];
    }
}

public class Solution {
    public int Search(int[] secret, int target) => Search(new ArrayReader(secret), target);

    public int Search(ArrayReader reader, int target) {
        int right = 1;
        while (reader.Get(right) < target) right <<= 1;
        int left = right >> 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int value = reader.Get(mid);
            if (value == target) return mid;
            if (value > target) right = mid - 1;
            else left = mid + 1;
        }
        return -1;
    }
}
