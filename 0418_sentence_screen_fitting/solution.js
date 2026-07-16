// LeetCode 0418 - Sentence Screen Fitting
var wordsTyping = function (sentence, rows, cols) {
    let count = 0;
    let index = 0;
    const total = sentence.length;
    for (let row = 0; row < rows; row += 1) {
        let col = 0;
        while (true) {
            const word = sentence[index];
            const needed = word.length + (col > 0 ? 1 : 0);
            if (col + needed > cols) break;
            if (col > 0) col += 1;
            col += word.length;
            index = (index + 1) % total;
            if (index === 0) count += 1;
        }
    }
    return count;
};

module.exports = { wordsTyping };
