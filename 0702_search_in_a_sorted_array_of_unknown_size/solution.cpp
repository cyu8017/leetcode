// LeetCode 0702 - Search in a Sorted Array of Unknown Size
// https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/

#include <vector>

class ArrayReader {
public:
    explicit ArrayReader(const std::vector<int>& secret) : secret_(secret) {}

    int get(int index) const {
        if (index < 0 || index >= static_cast<int>(secret_.size())) {
            return 2147483647;
        }
        return secret_[index];
    }

private:
    std::vector<int> secret_;
};

class Solution {
public:
    // Harness passes the secret array directly; wrap it as ArrayReader.
    int search(const std::vector<int>& secret, int target) {
        return search(ArrayReader(secret), target);
    }

    int search(const ArrayReader& reader, int target) {
        int right = 1;
        while (reader.get(right) < target) {
            right <<= 1;
        }
        int left = right >> 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int value = reader.get(mid);
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
};
