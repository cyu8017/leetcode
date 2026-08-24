// LeetCode 2024 - Maximize the Confusion of an Exam
// https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

export function maxConsecutiveAnswers(answerKey: string, k: number): number {
    const maxWith = (ch) => {
        let left = 0, bad = 0, best = 0;
        for (let right = 0; right < answerKey.length; right++) {
            if (answerKey[right] !== ch) bad++;
            while (bad > k) {
                if (answerKey[left] !== ch) bad--;
                left++;
            }
            best = Math.max(best, right - left + 1);
        }
        return best;
    };
    return Math.max(maxWith('T'), maxWith('F'));
}
