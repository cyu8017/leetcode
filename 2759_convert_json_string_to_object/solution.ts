// LeetCode 2759 - Convert JSON String to Object
// https://leetcode.com/problems/convert-json-string-to-object/

export function jsonParse(str: string): any {
    let i = 0;
    const parse = () => {
        if (str[i] === '"') {
            i++;
            let s = '';
            while (str[i] !== '"') s += str[i++];
            i++;
            return s;
        }
        if (str[i] === 't') { i += 4; return true; }
        if (str[i] === 'f') { i += 5; return false; }
        if (str[i] === 'n') { i += 4; return null; }
        if (str[i] === '[') {
            i++;
            const arr = [];
            if (str[i] === ']') { i++; return arr; }
            while (true) {
                arr.push(parse());
                if (str[i] === ',') { i++; continue; }
                i++; // ]
                return arr;
            }
        }
        if (str[i] === '{') {
            i++;
            const obj = {};
            if (str[i] === '}') { i++; return obj; }
            while (true) {
                const key = parse();
                i++; // :
                obj[key] = parse();
                if (str[i] === ',') { i++; continue; }
                i++; // }
                return obj;
            }
        }
        let start = i;
        if (str[i] === '-') i++;
        while (i < str.length && ((str[i] >= '0' && str[i] <= '9') || str[i] === '.')) i++;
        return Number(str.slice(start, i));
    }    return parse();
};
