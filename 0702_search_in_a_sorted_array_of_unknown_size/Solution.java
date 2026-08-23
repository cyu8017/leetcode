// LeetCode 0702 - Search in a Sorted Array of Unknown Size
// https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/

class ArrayReader {
    private final int[] secret;
    ArrayReader(int[] secret) { this.secret = secret; }
    public int get(int index) {
        if (index < 0 || index >= secret.length) return 2147483647;
        return secret[index];
    }
}

class Solution {
    public int search(int[] secret, int target) {
        return search(new ArrayReader(secret), target);
    }

    public int search(ArrayReader reader, int target) {
        int right = 1;
        while (reader.get(right) < target) right <<= 1;
        int left = right >> 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int value = reader.get(mid);
            if (value == target) return mid;
            if (value > target) right = mid - 1;
            else left = mid + 1;
        }
        return -1;
    }
}
