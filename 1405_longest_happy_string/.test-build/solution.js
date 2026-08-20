"use strict";
// LeetCode 1405: Longest Happy String
function longestDiverseString(a, b, c) {
    const counts = [["a", a], ["b", b], ["c", c]], result = [];
    while (true) {
        counts.sort((x, y) => y[1] - x[1]);
        const [ch, count] = counts[0];
        if (!count)
            break;
        if (result.length >= 2 && result.at(-1) === ch && result.at(-2) === ch) {
            if (!counts[1][1])
                break;
            result.push(counts[1][0]);
            counts[1][1]--;
        }
        else {
            result.push(ch);
            counts[0][1]--;
        }
    }
    return result.join("");
}
