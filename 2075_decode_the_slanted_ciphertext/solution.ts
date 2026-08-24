// LeetCode 2075 - Decode the Slanted Ciphertext
// https://leetcode.com/problems/decode-the-slanted-ciphertext/

export function decodeCiphertext(encodedText: string, rows: number): string {
    if (rows === 1) return encodedText;
    const cols = encodedText.length / rows;
    let b = "";
    for (let c = 0; c < cols; c++)
        for (let r = 0; r < rows && c + r < cols; r++)
            b += encodedText[r * cols + c + r];
    while (b.length > 0 && b[b.length - 1] === ' ') b = b.slice(0, -1);
    return b;
}
