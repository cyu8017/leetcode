// LeetCode 2018 - Check if Word Can Be Placed In Crossword
// https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/

/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var placeWordInCrossword = function(board, word) {
    const m = board.length, n = board[0].length, L = word.length;
    const match = (cells) => {
        if (cells.length !== L) return false;
        let ok1 = true, ok2 = true;
        for (let i = 0; i < L; i++) {
            if (cells[i] !== ' ' && cells[i] !== word[i]) ok1 = false;
            if (cells[i] !== ' ' && cells[i] !== word[L - 1 - i]) ok2 = false;
        }
        return ok1 || ok2;
    };
    for (let r = 0; r < m; r++) {
        let c = 0;
        while (c < n) {
            while (c < n && board[r][c] === '#') c++;
            const start = c;
            while (c < n && board[r][c] !== '#') c++;
            if (c - start === L) {
                let sb = "";
                for (let i = start; i < c; i++) sb += board[r][i];
                if (match(sb)) return true;
            }
        }
    }
    for (let c = 0; c < n; c++) {
        let r = 0;
        while (r < m) {
            while (r < m && board[r][c] === '#') r++;
            const start = r;
            while (r < m && board[r][c] !== '#') r++;
            if (r - start === L) {
                let sb = "";
                for (let i = 0; i < L; i++) sb += board[start + i][c];
                if (match(sb)) return true;
            }
        }
    }
    return false;
};
