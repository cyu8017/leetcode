// LeetCode 0408 - Valid Word Abbreviation
export function validWordAbbreviation(word: string, abbr: string): boolean {
    let i = 0;
    let j = 0;
    while (i < word.length && j < abbr.length) {
        if (abbr[j] >= "0" && abbr[j] <= "9") {
            if (abbr[j] === "0") return false;
            let number = 0;
            while (j < abbr.length && abbr[j] >= "0" && abbr[j] <= "9") {
                number = number * 10 + Number(abbr[j]);
                j += 1;
            }
            i += number;
        } else {
            if (word[i] !== abbr[j]) return false;
            i += 1;
            j += 1;
        }
    }
    return i === word.length && j === abbr.length;
}
