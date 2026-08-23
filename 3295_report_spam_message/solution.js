// LeetCode 3295 - Report Spam Message
// https://leetcode.com/problems/report-spam-message/

var reportSpam = function(message, bannedWords) {
    const ban = new Set(bannedWords);
    let cnt = 0;
    for (const w of message) {
        if (ban.has(w)) {
            cnt++;
            if (cnt >= 2) return true;
        }
    }
    return false;
};
