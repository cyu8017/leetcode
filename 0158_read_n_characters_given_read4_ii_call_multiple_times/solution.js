// LeetCode 0158 - Read N Characters Given read4 II - Call Multiple Times
// https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/

/**
 * Simulates repeated read calls while retaining unused read4 characters.
 * @param {string} file
 * @param {number[]} queries
 * @return {number[]}
 */
var read = function(file, queries) {
    let fileIndex = 0;
    const buffer = [];
    let bufferIndex = 0;
    let bufferSize = 0;

    /**
     * @return {number}
     */
    const read4 = function() {
        bufferSize = 0;
        bufferIndex = 0;
        while (bufferSize < 4 && fileIndex < file.length) {
            buffer[bufferSize] = file[fileIndex];
            fileIndex += 1;
            bufferSize += 1;
        }
        return bufferSize;
    };

    /**
     * @param {number} n
     * @return {number}
     */
    const readOnce = function(n) {
        let copied = 0;
        while (copied < n) {
            if (bufferIndex === bufferSize && read4() === 0) break;
            while (copied < n && bufferIndex < bufferSize) {
                copied += 1;
                bufferIndex += 1;
            }
        }
        return copied;
    };

    return queries.map(readOnce);
};