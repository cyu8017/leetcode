// LeetCode 1535 - Find the Winner of an Array Game
// https://leetcode.com/problems/find-the-winner-of-an-array-game/

#include <vector>

class Solution {
public:
    int getWinner(std::vector<int>& arr, int k) {
        int champion = arr[0];
        int wins = 0;
        for (std::size_t i = 1; i < arr.size(); ++i) {
            int challenger = arr[i];
            if (champion > challenger) {
                wins += 1;
            } else {
                champion = challenger;
                wins = 1;
            }
            if (wins == k) {
                break;
            }
        }
        return champion;
    }
};
