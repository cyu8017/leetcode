// LeetCode 1006 - Clumsy Factorial
// https://leetcode.com/problems/clumsy-factorial/
function clumsy(n) {
    const stack = [n];
    n -= 1;
    let op = 0;
    while (n > 0) {
        if (op % 4 === 0) {
            stack.push(stack.pop() * n);
        }
        else if (op % 4 === 1) {
            stack.push(Math.trunc(stack.pop() / n));
        }
        else if (op % 4 === 2) {
            stack.push(n);
        }
        else {
            stack.push(-n);
        }
        n -= 1;
        op += 1;
    }
    return stack.reduce((a, b) => a + b, 0);
}
