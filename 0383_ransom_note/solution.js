// LeetCode 0383 - Ransom Note
var canConstruct = function (ransomNote, magazine) {
    const counts = new Map();
    for (const char of magazine) {
        counts.set(char, (counts.get(char) || 0) + 1);
    }
    for (const char of ransomNote) {
        const remaining = counts.get(char) || 0;
        if (remaining === 0) return false;
        counts.set(char, remaining - 1);
    }
    return true;
};

module.exports = { canConstruct };
