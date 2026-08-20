"use strict";
function findMaxValueOfEquation(points, k) {
    const deque = [];
    let head = 0, answer = -Infinity;
    for (const [x, y] of points) {
        while (head < deque.length && x - deque[head][0] > k)
            head++;
        if (head < deque.length)
            answer = Math.max(answer, x + y + deque[head][1]);
        const value = y - x;
        while (deque.length > head && deque[deque.length - 1][1] <= value)
            deque.pop();
        deque.push([x, value]);
    }
    return answer;
}
