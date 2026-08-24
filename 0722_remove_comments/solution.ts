// LeetCode 0722 - Remove Comments
// https://leetcode.com/problems/remove-comments/

export function removeComments(source: string[]): string[] {
    const result = [];
    let buffer = '';
    let inBlock = false;
    for (const line of source) {
        let i = 0;
        while (i < line.length) {
            if (inBlock) {
                if (i + 1 < line.length && line[i] === '*' && line[i + 1] === '/') {
                    inBlock = false;
                    i += 2;
                } else i++;
            } else if (i + 1 < line.length && line[i] === '/' && line[i + 1] === '*') {
                inBlock = true;
                i += 2;
            } else if (i + 1 < line.length && line[i] === '/' && line[i + 1] === '/') break;
            else buffer += line[i++];
        }
        if (!inBlock && buffer.length > 0) {
            result.push(buffer);
            buffer = '';
        }
    }
    return result;
}
