// LeetCode 0068 - Text Justification
// https://leetcode.com/problems/text-justification/

/**
 * @param {string[]} words
 * @param {number} maxWidth
 * @return {string[]}
 */
var fullJustify = function(words, maxWidth) {
    const result = [];
    let i = 0;

    while (i < words.length) {
        const lineWords = [];
        let lineLen = 0;

        while (i < words.length) {
            const word = words[i];
            const extra = lineWords.length > 0 ? 1 : 0;
            if (lineLen + word.length + extra > maxWidth) {
                break;
            }
            lineWords.push(word);
            lineLen += word.length + extra;
            i++;
        }

        if (i === words.length || lineWords.length === 1) {
            let line = lineWords.join(' ');
            line += ' '.repeat(maxWidth - line.length);
            result.push(line);
        } else {
            const totalChars = lineWords.reduce((sum, w) => sum + w.length, 0);
            const totalSpaces = maxWidth - totalChars;
            const gaps = lineWords.length - 1;
            const space = Math.floor(totalSpaces / gaps);
            const remainder = totalSpaces % gaps;
            let line = '';
            for (let j = 0; j < lineWords.length - 1; j++) {
                line += lineWords[j] + ' '.repeat(space + (j < remainder ? 1 : 0));
            }
            line += lineWords[lineWords.length - 1];
            result.push(line);
        }
    }

    return result;
};
