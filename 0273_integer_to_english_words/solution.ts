// LeetCode 0273 - Integer to English Words
// https://leetcode.com/problems/integer-to-english-words/

const ONES = [
    "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
    "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
    "Seventeen", "Eighteen", "Nineteen",
];
const TENS = [
    "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety",
];
const THOUSANDS = ["", "Thousand", "Million", "Billion"];

function numberToWords(num: number): string {
    if (num === 0) {
        return "Zero";
    }

    const convertChunk = (value: number): string => {
        if (value === 0) {
            return "";
        }
        if (value < 20) {
            return ONES[value];
        }
        if (value < 100) {
            const tens = TENS[Math.floor(value / 10)];
            const ones = ONES[value % 10];
            return ones ? `${tens} ${ones}` : tens;
        }
        const hundreds = ONES[Math.floor(value / 100)];
        const remainder = convertChunk(value % 100);
        return remainder ? `${hundreds} Hundred ${remainder}` : `${hundreds} Hundred`;
    };

    const parts: string[] = [];
    let chunkIndex = 0;
    while (num > 0) {
        const chunk = num % 1000;
        if (chunk) {
            let chunkWords = convertChunk(chunk);
            if (THOUSANDS[chunkIndex]) {
                chunkWords += ` ${THOUSANDS[chunkIndex]}`;
            }
            parts.push(chunkWords);
        }
        num = Math.floor(num / 1000);
        chunkIndex += 1;
    }
    return parts.reverse().join(" ");
}
