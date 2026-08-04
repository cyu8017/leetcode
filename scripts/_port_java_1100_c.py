#!/usr/bin/env python3
"""Port Java solutions batch C (1150-1185)."""
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
S: dict[str, str] = {}

S["1150_check_if_a_number_is_majority_element_in_a_sorted_array"] = r"""// LeetCode 1150 - Check If a Number Is Majority Element in a Sorted Array
// https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/

class Solution {
    public boolean isMajorityElement(int[] nums, int target) {
        int left = lowerBound(nums, target);
        int right = lowerBound(nums, target + 1);
        return right - left > nums.length / 2;
    }
    private int lowerBound(int[] nums, int target) {
        int lo = 0, hi = nums.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (nums[mid] < target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
"""

S["1151_minimum_swaps_to_group_all_1s_together"] = r"""// LeetCode 1151 - Minimum Swaps to Group All 1's Together
// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/

class Solution {
    public int minSwaps(int[] data) {
        int ones = 0;
        for (int x : data) ones += x;
        if (ones <= 1) return 0;
        int cur = 0;
        for (int i = 0; i < ones; i++) cur += data[i];
        int best = cur;
        for (int i = ones; i < data.length; i++) {
            cur += data[i] - data[i - ones];
            best = Math.max(best, cur);
        }
        return ones - best;
    }
}
"""

S["1152_analyze_user_website_visit_pattern"] = r"""// LeetCode 1152 - Analyze User Website Visit Pattern
// https://leetcode.com/problems/analyze-user-website-visit-pattern/

import java.util.*;

class Solution {
    public List<String> mostVisitedPattern(String[] username, int[] timestamp, String[] website) {
        Map<String, List<int[]>> visits = new HashMap<>();
        for (int i = 0; i < username.length; i++) {
            visits.computeIfAbsent(username[i], k -> new ArrayList<>()).add(new int[]{timestamp[i], i});
        }
        Map<String, Integer> scores = new HashMap<>();
        for (List<int[]> list : visits.values()) {
            list.sort((a, b) -> Integer.compare(a[0], b[0]));
            List<String> sites = new ArrayList<>();
            for (int[] p : list) sites.add(website[p[1]]);
            Set<String> patterns = new HashSet<>();
            int m = sites.size();
            for (int i = 0; i < m; i++)
                for (int j = i + 1; j < m; j++)
                    for (int k = j + 1; k < m; k++)
                        patterns.add(sites.get(i) + "," + sites.get(j) + "," + sites.get(k));
            for (String p : patterns) scores.merge(p, 1, Integer::sum);
        }
        String best = null;
        int bestCount = -1;
        for (Map.Entry<String, Integer> e : scores.entrySet()) {
            if (e.getValue() > bestCount || (e.getValue() == bestCount && (best == null || e.getKey().compareTo(best) < 0))) {
                bestCount = e.getValue();
                best = e.getKey();
            }
        }
        return Arrays.asList(best.split(",", -1));
    }
}
"""

S["1153_string_transforms_into_another_string"] = r"""// LeetCode 1153 - String Transforms Into Another String
// https://leetcode.com/problems/string-transforms-into-another-string/

import java.util.*;

class Solution {
    public boolean canConvert(String str1, String str2) {
        if (str1.equals(str2)) return true;
        Map<Character, Character> mapping = new HashMap<>();
        for (int i = 0; i < str1.length(); i++) {
            char a = str1.charAt(i), b = str2.charAt(i);
            if (mapping.containsKey(a) && mapping.get(a) != b) return false;
            mapping.put(a, b);
        }
        Set<Character> uniq = new HashSet<>();
        for (char c : str2.toCharArray()) uniq.add(c);
        return uniq.size() < 26;
    }
}
"""

S["1154_day_of_the_year"] = r"""// LeetCode 1154 - Day of the Year
// https://leetcode.com/problems/day-of-the-year/

class Solution {
    public int dayOfYear(String date) {
        String[] parts = date.split("-");
        int year = Integer.parseInt(parts[0]);
        int month = Integer.parseInt(parts[1]);
        int day = Integer.parseInt(parts[2]);
        boolean leap = year % 4 == 0 && (year % 100 != 0 || year % 400 == 0);
        int[] days = {31, leap ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int ans = day;
        for (int i = 0; i < month - 1; i++) ans += days[i];
        return ans;
    }
}
"""

S["1155_number_of_dice_rolls_with_target_sum"] = r"""// LeetCode 1155 - Number of Dice Rolls With Target Sum
// https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

class Solution {
    public int numRollsToTarget(int n, int k, int target) {
        final int MOD = 1_000_000_007;
        int[] dp = new int[target + 1];
        dp[0] = 1;
        for (int dice = 0; dice < n; dice++) {
            int[] next = new int[target + 1];
            for (int s = 0; s <= target; s++) {
                if (dp[s] == 0) continue;
                for (int face = 1; face <= k && s + face <= target; face++) {
                    next[s + face] = (next[s + face] + dp[s]) % MOD;
                }
            }
            dp = next;
        }
        return dp[target];
    }
}
"""

S["1156_swap_for_longest_repeated_character_substring"] = r"""// LeetCode 1156 - Swap For Longest Repeated Character Substring
// https://leetcode.com/problems/swap-for-longest-repeated-character-substring/

class Solution {
    public int maxRepOpt1(String text) {
        int[] count = new int[26];
        for (char c : text.toCharArray()) count[c - 'a']++;
        int n = text.length(), ans = 0, i = 0;
        while (i < n) {
            int j = i;
            while (j < n && text.charAt(j) == text.charAt(i)) j++;
            int length = j - i;
            int k = j + 1;
            while (k < n && text.charAt(k) == text.charAt(i)) k++;
            int length2 = j < n ? k - j - 1 : 0;
            ans = Math.max(ans, Math.min(length + length2 + 1, count[text.charAt(i) - 'a']));
            i = j;
        }
        return ans;
    }
}
"""

S["1157_online_majority_element_in_subarray"] = r"""// LeetCode 1157 - Online Majority Element In Subarray
// https://leetcode.com/problems/online-majority-element-in-subarray/

import java.util.*;

class MajorityChecker {
    private final int[] arr;
    private final Map<Integer, List<Integer>> pos = new HashMap<>();

    public MajorityChecker(int[] arr) {
        this.arr = arr;
        for (int i = 0; i < arr.length; i++) {
            pos.computeIfAbsent(arr[i], k -> new ArrayList<>()).add(i);
        }
    }

    public int query(int left, int right, int threshold) {
        int candidate = 0, count = 0;
        for (int i = left; i <= right; i++) {
            if (count == 0) candidate = arr[i];
            count += arr[i] == candidate ? 1 : -1;
        }
        List<Integer> locs = pos.get(candidate);
        int freq = upperBound(locs, right) - lowerBound(locs, left);
        return freq >= threshold ? candidate : -1;
    }

    private int lowerBound(List<Integer> a, int t) {
        int lo = 0, hi = a.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a.get(mid) < t) lo = mid + 1; else hi = mid;
        }
        return lo;
    }

    private int upperBound(List<Integer> a, int t) {
        int lo = 0, hi = a.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a.get(mid) <= t) lo = mid + 1; else hi = mid;
        }
        return lo;
    }
}
"""

S["1160_find_words_that_can_be_formed_by_characters"] = r"""// LeetCode 1160 - Find Words That Can Be Formed by Characters
// https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

class Solution {
    public int countCharacters(String[] words, String chars) {
        int[] avail = new int[26];
        for (char c : chars.toCharArray()) avail[c - 'a']++;
        int ans = 0;
        for (String word : words) {
            int[] need = new int[26];
            boolean ok = true;
            for (char c : word.toCharArray()) {
                if (++need[c - 'a'] > avail[c - 'a']) { ok = false; break; }
            }
            if (ok) ans += word.length();
        }
        return ans;
    }
}
"""

S["1161_maximum_level_sum_of_a_binary_tree"] = r"""// LeetCode 1161 - Maximum Level Sum of a Binary Tree
// https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public int maxLevelSum(TreeNode root) {
        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.offer(root);
        int bestSum = Integer.MIN_VALUE, bestLevel = 1, level = 1;
        while (!queue.isEmpty()) {
            int total = 0, size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                total += node.val;
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            if (total > bestSum) {
                bestSum = total;
                bestLevel = level;
            }
            level++;
        }
        return bestLevel;
    }
}
"""


def main():
    for name, content in S.items():
        (ROOT / name / "solution.java").write_text(content, encoding="utf-8", newline="\n")
        print("wrote", name)
    print("done", len(S))

if __name__ == "__main__":
    main()
