// LeetCode 0336 - Palindrome Pairs
var palindromePairs = function(words) {
    const wordMap = new Map(words.map((word, index) => [word, index]));
    const result = new Set();

    for (let index = 0; index < words.length; index += 1) {
        const word = words[index];
        for (let split = 0; split <= word.length; split += 1) {
            const left = word.slice(0, split);
            const right = word.slice(split);
            const reversedLeft = left.split("").reverse().join("");
            const reversedRight = right.split("").reverse().join("");

            if (left === reversedLeft && wordMap.has(reversedRight) && wordMap.get(reversedRight) !== index) {
                result.add(`${wordMap.get(reversedRight)},${index}`);
            }
            if (right === reversedRight && wordMap.has(reversedLeft) && wordMap.get(reversedLeft) !== index) {
                result.add(`${index},${wordMap.get(reversedLeft)}`);
            }
        }
    }

    return [...result].map((pair) => pair.split(",").map(Number));
};
