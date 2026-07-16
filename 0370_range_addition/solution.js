// LeetCode 0370 - Range Addition
var getModifiedArray = function(length, updates) {
    const diff = Array(length + 1).fill(0);
    for (const [start, end, inc] of updates) {
        diff[start] += inc;
        if (end + 1 < diff.length) diff[end + 1] -= inc;
    }

    const result = Array(length).fill(0);
    let running = 0;
    for (let index = 0; index < length; index += 1) {
        running += diff[index];
        result[index] = running;
    }
    return result;
};
