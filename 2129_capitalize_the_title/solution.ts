// LeetCode 2129 - Capitalize the Title
// https://leetcode.com/problems/capitalize-the-title/

export function capitalizeTitle(title: string): string {
    const parts = title.trim().split(/\s+/);
    for (let i = 0; i < parts.length; i++) {
        let w = parts[i].toLowerCase();
        if (w.length > 2) w = w[0].toUpperCase() + w.slice(1);
        parts[i] = w;
    }
    return parts.join(' ');
}
