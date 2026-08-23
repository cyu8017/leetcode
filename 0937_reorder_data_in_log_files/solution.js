// LeetCode 0937 - Reorder Data in Log Files
// https://leetcode.com/problems/reorder-data-in-log-files/

/**
 * @param {string[]} logs
 * @return {string[]}
 */
var reorderLogFiles = function(logs) {
    const letter = [], digit = [];
    for (const log of logs) {
        const i = log.indexOf(" ");
        if (log[i + 1] >= "0" && log[i + 1] <= "9") digit.push(log);
        else letter.push(log);
    }
    letter.sort((a, b) => {
        const ia = a.indexOf(" "), ib = b.indexOf(" ");
        const ca = a.slice(ia + 1), cb = b.slice(ib + 1);
        if (ca !== cb) return ca < cb ? -1 : 1;
        const ida = a.slice(0, ia), idb = b.slice(0, ib);
        return ida < idb ? -1 : ida > idb ? 1 : 0;
    });
    return letter.concat(digit);
};
