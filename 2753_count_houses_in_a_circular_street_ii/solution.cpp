// LeetCode 2753 - Count Houses in a Circular Street II
// https://leetcode.com/problems/count-houses-in-a-circular-street-ii/

#include <vector>

class Solution {
public:
    int houseCount(std::vector<int>& street, int k) {
        int n = (int)street.size();
        if (n == 0) return 0;
        int start = -1;
        for (int i = 0; i < n; i++) {
            if (street[i] == 1) { start = i; break; }
        }
        if (start < 0) return 0;
        int count = 1, moves = 0, i = start;
        while (moves < k) {
            i = (i + 1) % n;
            moves++;
            if (i == start) break;
            if (street[i] == 1) count++;
        }
        return count;
    }
};
