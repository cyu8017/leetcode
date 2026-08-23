// LeetCode 1533 - Find the Index of the Large Integer
// https://leetcode.com/problems/find-the-index-of-the-large-integer/

#include <vector>

class ArrayReader {
public:
    explicit ArrayReader(const std::vector<int>& arr) : arr_(arr) {}

    int compareSub(int l, int r, int x, int y) const {
        long long a = 0;
        long long b = 0;
        for (int i = l; i <= r; ++i) {
            a += arr_[i];
        }
        for (int i = x; i <= y; ++i) {
            b += arr_[i];
        }
        return (a > b) - (a < b);
    }

    int length() const {
        return static_cast<int>(arr_.size());
    }

private:
    std::vector<int> arr_;
};

class Solution {
public:
    // Harness passes the secret array directly; wrap it as ArrayReader.
    int getIndex(const std::vector<int>& arr) {
        ArrayReader reader(arr);
        return getIndex(reader);
    }

    int getIndex(ArrayReader& reader) {
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
};
