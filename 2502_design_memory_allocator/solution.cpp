// LeetCode 2502 - Design Memory Allocator
// https://leetcode.com/problems/design-memory-allocator/

#include <vector>

class Allocator {
    std::vector<int> mem;
public:
    Allocator(int n) : mem(n, 0) {}

    int allocate(int size, int mID) {
        int freeCnt = 0;
        for (int i = 0; i < (int)mem.size(); i++) {
            if (mem[i] == 0) {
                freeCnt++;
                if (freeCnt == size) {
                    int start = i - size + 1;
                    for (int j = start; j <= i; j++) mem[j] = mID;
                    return start;
                }
            } else {
                freeCnt = 0;
            }
        }
        return -1;
    }

    int freeMemory(int mID) {
        int cnt = 0;
        for (int& x : mem) {
            if (x == mID) {
                x = 0;
                cnt++;
            }
        }
        return cnt;
    }
};
