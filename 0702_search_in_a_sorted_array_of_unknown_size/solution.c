// LeetCode 0702 - Search in a Sorted Array of Unknown Size
// https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/

struct ArrayReader;

/* Forward declaration of ArrayReader API (provided by judge). */
int get(struct ArrayReader* reader, int index);

int search(struct ArrayReader* reader, int target) {
    int right = 1;
    while (get(reader, right) < target) {
        right <<= 1;
    }
    int left = right >> 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        int value = get(reader, mid);
        if (value == target) {
            return mid;
        }
        if (value > target) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return -1;
}
