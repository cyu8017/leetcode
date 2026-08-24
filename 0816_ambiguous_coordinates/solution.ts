// LeetCode 0816 - Ambiguous Coordinates
// https://leetcode.com/problems/ambiguous-coordinates/

export function ambiguousCoordinates(s: string): string[] {
    const digits = s.substring(1, s.length - 1);
    const candidates = (frag) => {
        const options = [];
        if (!frag.length || (frag.length > 1 && frag[0] === '0' && frag[frag.length - 1] === '0')) return options;
        if (frag[0] === '0' && frag.length > 1) {
            if (frag[frag.length - 1] !== '0') options.push("0." + frag.substring(1));
            return options;
        }
        options.push(frag);
        if (frag[frag.length - 1] === '0') return options;
        for (let i = 1; i < frag.length; i++) {
            options.push(frag.substring(0, i) + "." + frag.substring(i));
        }
        return options;
    };
    const answer = [];
    for (let i = 1; i < digits.length; i++) {
        for (const left of candidates(digits.substring(0, i))) {
            for (const right of candidates(digits.substring(i))) {
                answer.push("(" + left + ", " + right + ")");
            }
        }
    }
    return answer;
}
