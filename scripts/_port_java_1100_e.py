#!/usr/bin/env python3
"""Port Java batch E: 1175-1201."""
from __future__ import annotations
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
S: dict[str, str] = {}

S["1175_prime_arrangements"] = r"""// LeetCode 1175 - Prime Arrangements
// https://leetcode.com/problems/prime-arrangements/

class Solution {
    public int numPrimeArrangements(int n) {
        final int MOD = 1_000_000_007;
        int primes = 0;
        for (int i = 1; i <= n; i++) if (isPrime(i)) primes++;
        return (int) (fact(primes, MOD) * fact(n - primes, MOD) % MOD);
    }
    private boolean isPrime(int x) {
        if (x < 2) return false;
        for (int d = 2; d * d <= x; d++) if (x % d == 0) return false;
        return true;
    }
    private long fact(int n, int MOD) {
        long ans = 1;
        for (int i = 2; i <= n; i++) ans = ans * i % MOD;
        return ans;
    }
}
"""

S["1176_diet_plan_performance"] = r"""// LeetCode 1176 - Diet Plan Performance
// https://leetcode.com/problems/diet-plan-performance/

class Solution {
    public int dietPlanPerformance(int[] calories, int k, int lower, int upper) {
        int window = 0;
        for (int i = 0; i < k; i++) window += calories[i];
        int ans = 0;
        if (window < lower) ans--;
        else if (window > upper) ans++;
        for (int i = k; i < calories.length; i++) {
            window += calories[i] - calories[i - k];
            if (window < lower) ans--;
            else if (window > upper) ans++;
        }
        return ans;
    }
}
"""

S["1177_can_make_palindrome_from_substring"] = r"""// LeetCode 1177 - Can Make Palindrome from Substring
// https://leetcode.com/problems/can-make-palindrome-from-substring/

import java.util.*;

class Solution {
    public List<Boolean> canMakePaliQueries(String s, int[][] queries) {
        int[] prefix = new int[s.length() + 1];
        int mask = 0;
        for (int i = 0; i < s.length(); i++) {
            mask ^= 1 << (s.charAt(i) - 'a');
            prefix[i + 1] = mask;
        }
        List<Boolean> ans = new ArrayList<>();
        for (int[] q : queries) {
            int bits = Integer.bitCount(prefix[q[1] + 1] ^ prefix[q[0]]);
            ans.add(bits / 2 <= q[2]);
        }
        return ans;
    }
}
"""

S["1178_number_of_valid_words_for_each_puzzle"] = r"""// LeetCode 1178 - Number of Valid Words for Each Puzzle
// https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

import java.util.*;

class Solution {
    public List<Integer> findNumOfValidWords(String[] words, String[] puzzles) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (String w : words) freq.merge(maskOf(w), 1, Integer::sum);
        List<Integer> ans = new ArrayList<>();
        for (String puzzle : puzzles) {
            int first = 1 << (puzzle.charAt(0) - 'a');
            int full = maskOf(puzzle);
            int sub = full, total = 0;
            while (true) {
                if ((sub & first) != 0) total += freq.getOrDefault(sub, 0);
                if (sub == 0) break;
                sub = (sub - 1) & full;
            }
            ans.add(total);
        }
        return ans;
    }
    private int maskOf(String s) {
        int mask = 0;
        for (char ch : s.toCharArray()) mask |= 1 << (ch - 'a');
        return mask;
    }
}
"""

S["1180_count_substrings_with_only_one_distinct_letter"] = r"""// LeetCode 1180 - Count Substrings with Only One Distinct Letter
// https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/

class Solution {
    public int countLetters(String s) {
        int ans = 1, length = 1;
        for (int i = 1; i < s.length(); i++) {
            length = s.charAt(i) == s.charAt(i - 1) ? length + 1 : 1;
            ans += length;
        }
        return ans;
    }
}
"""

S["1181_before_and_after_puzzle"] = r"""// LeetCode 1181 - Before and After Puzzle
// https://leetcode.com/problems/before-and-after-puzzle/

import java.util.*;

class Solution {
    public List<String> beforeAndAfterPuzzles(String[] phrases) {
        String[][] split = new String[phrases.length][];
        for (int i = 0; i < phrases.length; i++) split[i] = phrases[i].split(" ");
        Set<String> result = new TreeSet<>();
        for (int i = 0; i < split.length; i++) {
            for (int j = 0; j < split.length; j++) {
                if (i == j) continue;
                if (split[i][split[i].length - 1].equals(split[j][0])) {
                    StringBuilder sb = new StringBuilder();
                    for (int k = 0; k < split[i].length; k++) {
                        if (k > 0) sb.append(' ');
                        sb.append(split[i][k]);
                    }
                    for (int k = 1; k < split[j].length; k++) {
                        sb.append(' ').append(split[j][k]);
                    }
                    result.add(sb.toString());
                }
            }
        }
        return new ArrayList<>(result);
    }
}
"""

S["1182_shortest_distance_to_target_color"] = r"""// LeetCode 1182 - Shortest Distance to Target Color
// https://leetcode.com/problems/shortest-distance-to-target-color/

import java.util.*;

class Solution {
    public List<Integer> shortestDistanceColor(int[] colors, int[][] queries) {
        Map<Integer, List<Integer>> pos = new HashMap<>();
        for (int i = 0; i < colors.length; i++) {
            pos.computeIfAbsent(colors[i], k -> new ArrayList<>()).add(i);
        }
        List<Integer> ans = new ArrayList<>();
        for (int[] q : queries) {
            int i = q[0], c = q[1];
            if (!pos.containsKey(c)) { ans.add(-1); continue; }
            List<Integer> arr = pos.get(c);
            int idx = Collections.binarySearch(arr, i);
            if (idx < 0) idx = -idx - 1;
            int best = Integer.MAX_VALUE;
            if (idx < arr.size()) best = Math.min(best, arr.get(idx) - i);
            if (idx > 0) best = Math.min(best, i - arr.get(idx - 1));
            ans.add(best == Integer.MAX_VALUE ? -1 : best);
        }
        return ans;
    }
}
"""

S["1183_maximum_number_of_ones"] = r"""// LeetCode 1183 - Maximum Number of Ones
// https://leetcode.com/problems/maximum-number-of-ones/

import java.util.*;

class Solution {
    public int maximumNumberOfOnes(int width, int height, int sideLength, int maxOnes) {
        List<Integer> counts = new ArrayList<>();
        for (int r = 0; r < sideLength; r++) {
            for (int c = 0; c < sideLength; c++) {
                int rows = (height - r + sideLength - 1) / sideLength;
                int cols = (width - c + sideLength - 1) / sideLength;
                counts.add(rows * cols);
            }
        }
        counts.sort(Collections.reverseOrder());
        int ans = 0;
        for (int i = 0; i < maxOnes && i < counts.size(); i++) ans += counts.get(i);
        return ans;
    }
}
"""

S["1184_distance_between_bus_stops"] = r"""// LeetCode 1184 - Distance Between Bus Stops
// https://leetcode.com/problems/distance-between-bus-stops/

class Solution {
    public int distanceBetweenBusStops(int[] distance, int start, int destination) {
        if (start > destination) { int t = start; start = destination; destination = t; }
        int clockwise = 0, total = 0;
        for (int i = 0; i < distance.length; i++) {
            total += distance[i];
            if (i >= start && i < destination) clockwise += distance[i];
        }
        return Math.min(clockwise, total - clockwise);
    }
}
"""

S["1185_day_of_the_week"] = r"""// LeetCode 1185 - Day of the Week
// https://leetcode.com/problems/day-of-the-week/

import java.time.*;

class Solution {
    public String dayOfTheWeek(int day, int month, int year) {
        return LocalDate.of(year, month, day).getDayOfWeek()
            .getDisplayName(java.time.format.TextStyle.FULL, Locale.US);
    }
}
"""

def main():
    for name, content in S.items():
        path = ROOT / name / "solution.java"
        if not path.parent.exists():
            print("skip missing", name)
            continue
        # only overwrite stubs
        cur = path.read_text(encoding="utf-8") if path.exists() else ""
        if "void solve()" not in cur and cur.strip() and "class " in cur and "solve()" not in cur:
            # already ported - still overwrite if stub pattern
            pass
        if "void solve()" in cur or not cur.strip() or len(cur) < 120:
            path.write_text(content, encoding="utf-8", newline="\n")
            print("wrote", name)
        else:
            print("skip done", name)
    print("done", len(S))

if __name__ == "__main__":
    main()
