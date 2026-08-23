// LeetCode 0157 - Read N Characters Given Read4
// https://leetcode.com/problems/read-n-characters-given-read4/

/**
 * Simulates read4 and returns how many characters can be read once.
 * @param {string} file
 * @param {number} n
 * @return {number}
 */
var read = function(file, n) {
    let fileIndex = 0;

    /**
     * @param {string[]} buffer
     * @return {number}
     */
    const read4 = function(buffer) {
        let count = 0;
        while (count < 4 && fileIndex < file.length) {
            buffer[count] = file[fileIndex];
            fileIndex += 1;
            count += 1;
        }
        return count;
    };

    let copied = 0;
    while (copied < n) {
        const buffer = [];
        const count = read4(buffer);
        if (count === 0) break;
        copied += Math.min(count, n - copied);
    }

    return copied;
};