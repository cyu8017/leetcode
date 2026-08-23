// LeetCode 3360 - Stone Removal Game
// https://leetcode.com/problems/stone-removal-game/

class Solution {
public:
    bool canAliceWin(int n) {
        int take = 10;
        bool alice = true;
        while (n >= take && take > 0) {
            n -= take;
            take--;
            alice = !alice;
        }
        return !alice;
    }
};
