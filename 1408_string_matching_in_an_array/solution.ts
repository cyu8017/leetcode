// LeetCode 1408: String Matching In An Array

function stringMatching(words: any): any {
    return words.filter((word, i: any): any => words.some((other, j: any): any => i !== j && other.includes(word)));
}
