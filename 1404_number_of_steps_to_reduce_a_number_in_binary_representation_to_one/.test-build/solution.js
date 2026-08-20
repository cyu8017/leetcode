"use strict";
// LeetCode 1404: Number Of Steps To Reduce A Number In Binary Representation To One
function numSteps(s) {
    let steps = 0, carry = 0;
    for (let i = s.length - 1; i > 0; i--) {
        const bit = Number(s[i]) + carry;
        if (bit === 1) {
            steps += 2;
            carry = 1;
        }
        else
            steps++;
    }
    return steps + carry;
}
