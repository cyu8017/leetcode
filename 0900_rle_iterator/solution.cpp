// LeetCode 0900 - RLE Iterator
// https://leetcode.com/problems/rle-iterator/

#include <vector>

class RLEIterator {
public:
    RLEIterator(std::vector<int>& encoding) : enc(encoding), i(0) {}

    int next(int n) {
        while (i < (int)enc.size()) {
            if (enc[i] >= n) {
                enc[i] -= n;
                return enc[i + 1];
            }
            n -= enc[i];
            i += 2;
        }
        return -1;
    }

private:
    std::vector<int> enc;
    int i;
};
