// LeetCode 1086 - High Five
// https://leetcode.com/problems/high-five/

function highFive(items: number[][]): number[][] {
    const scores = new Map<number, number[]>();
    for (const [studentId, score] of items) {
        if (!scores.has(studentId)) scores.set(studentId, []);
        scores.get(studentId)!.push(score);
    }
    const ans: number[][] = [];
    const ids = [...scores.keys()].sort((a, b) => a - b);
    for (const studentId of ids) {
        const top = scores.get(studentId)!.sort((a, b) => b - a).slice(0, 5);
        const avg = Math.floor(top.reduce((a, b) => a + b, 0) / 5);
        ans.push([studentId, avg]);
    }
    return ans;
}
