// LeetCode 0470 - Implement Rand10() Using Rand7()
// https://leetcode.com/problems/implement-rand10-using-rand7/

int rand7();

class Solution {
public:
    int rand10() {
        while (true) {
            int num = (rand7() - 1) * 7 + rand7();
            if (num <= 40) {
                return (num - 1) % 10 + 1;
            }
        }
    }
};
