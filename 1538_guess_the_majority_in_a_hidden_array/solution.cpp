// LeetCode 1538 - Guess the Majority in a Hidden Array
// https://leetcode.com/problems/guess-the-majority-in-a-hidden-array/

#include <vector>

class ArrayReader {
public:
    explicit ArrayReader(const std::vector<int>& nums) : nums_(nums) {}

    int query(int a, int b, int c, int d) const {
        int ones = nums_[a] + nums_[b] + nums_[c] + nums_[d];
        if (ones == 0 || ones == 4) {
            return 4;
        }
        if (ones == 1 || ones == 3) {
            return 2;
        }
        return 0;
    }

    int length() const {
        return static_cast<int>(nums_.size());
    }

private:
    std::vector<int> nums_;
};

class Solution {
public:
    // Harness passes the secret array directly; wrap it as ArrayReader.
    int guessMajority(const std::vector<int>& nums) {
        ArrayReader reader(nums);
        return guessMajority(reader);
    }

    int guessMajority(ArrayReader& reader) {
        int n = reader.length();
        int first_four = reader.query(0, 1, 2, 3);
        int shifted = reader.query(1, 2, 3, 4);
        int same = 1;
        int different = 0;
        int different_index = -1;
        int later_different = -1;
        bool four_same = first_four == shifted;
        if (four_same) {
            same += 1;
        } else {
            different += 1;
            different_index = 4;
        }
        int checks[3][4] = {{0, 2, 3, 4}, {0, 1, 3, 4}, {0, 1, 2, 4}};
        for (int index = 1; index <= 3; ++index) {
            if (reader.query(checks[index - 1][0], checks[index - 1][1], checks[index - 1][2],
                             checks[index - 1][3]) == shifted) {
                same += 1;
            } else {
                different += 1;
                different_index = index;
            }
        }
        for (int i = 5; i < n; ++i) {
            bool i_same_as_four = reader.query(1, 2, 3, i) == shifted;
            if (i_same_as_four == four_same) {
                same += 1;
            } else {
                different += 1;
                different_index = i;
                if (later_different == -1) {
                    later_different = i;
                }
            }
        }
        if (same == different) {
            return -1;
        }
        return same > different ? 0 : (later_different != -1 ? later_different : different_index);
    }
};
