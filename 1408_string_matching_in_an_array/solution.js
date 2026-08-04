// LeetCode 1408: String Matching In An Array

var stringMatching = function(words) {
    return words.filter((word, i) => words.some((other, j) => i !== j && other.includes(word)));
};
