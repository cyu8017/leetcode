// LeetCode 2424 - Longest Uploaded Prefix
// https://leetcode.com/problems/longest-uploaded-prefix/

#include <vector>

class LUPrefix {
public:
    LUPrefix(int n) : uploaded(n + 2, false), prefixLen(0) {}

    void upload(int video) {
        uploaded[video] = true;
        while (uploaded[prefixLen + 1]) prefixLen++;
    }

    int longest() {
        return prefixLen;
    }

private:
    std::vector<bool> uploaded;
    int prefixLen;
};
