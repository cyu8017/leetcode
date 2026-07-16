// LeetCode 0470 - Implement Rand10() Using Rand7()
// https://leetcode.com/problems/implement-rand10-using-rand7/

function rand7() {
    throw new Error("rand7 must be provided by the test harness");
}

class Solution {
    rand10() {
        while (true) {
            const num = (rand7() - 1) * 7 + rand7();
            if (num <= 40) return ((num - 1) % 10) + 1;
        }
    }
}

module.exports = { Solution, rand7 };
