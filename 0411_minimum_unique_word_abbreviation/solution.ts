// LeetCode 0411 - Minimum Unique Word Abbreviation
export function minAbbreviation(target: string, dictionary: string[]): string {
    const words = dictionary.filter((word) => word.length === target.length);
    let bestLen = target.length + 1;
    let result = target;

    const matches = (word: string, abbr: string): boolean => {
        let index = 0;
        let pointer = 0;
        while (index < word.length && pointer < abbr.length) {
            if (abbr[pointer] >= "0" && abbr[pointer] <= "9") {
                if (abbr[pointer] === "0") return false;
                let number = 0;
                while (pointer < abbr.length && abbr[pointer] >= "0" && abbr[pointer] <= "9") {
                    number = number * 10 + Number(abbr[pointer]);
                    pointer += 1;
                }
                index += number;
            } else {
                if (word[index] !== abbr[pointer]) return false;
                index += 1;
                pointer += 1;
            }
        }
        return index === word.length && pointer === abbr.length;
    };

    const valid = (abbr: string) => matches(target, abbr) && words.every((word) => !matches(word, abbr));

    const dfs = (index: number, parts: string[], skip: number): void => {
        if (index === target.length) {
            const abbr = parts.join("") + (skip ? String(skip) : "");
            if (valid(abbr) && (abbr.length < bestLen || (abbr.length === bestLen && abbr < result))) {
                bestLen = abbr.length;
                result = abbr;
            }
            return;
        }
        dfs(index + 1, parts, skip + 1);
        const next = [...parts];
        if (skip) next.push(String(skip));
        next.push(target[index]);
        dfs(index + 1, next, 0);
    };

    dfs(0, [], 0);
    return result;
}
