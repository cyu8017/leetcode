# LeetCode 0819 - Most Common Word
# https://leetcode.com/problems/most-common-word/

import re
from collections import Counter
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        words = re.findall(r"[a-z]+", paragraph.lower())
        counts = Counter(word for word in words if word not in banned_set)
        return counts.most_common(1)[0][0]
