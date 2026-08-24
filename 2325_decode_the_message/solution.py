# LeetCode 2325 - Decode the Message
# https://leetcode.com/problems/decode-the-message/


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mp = [0] * 26
        nxt = 97
        for c in key:
            if c == " " or mp[ord(c) - 97] != 0:
                continue
            mp[ord(c) - 97] = nxt
            nxt += 1
        out = list(message)
        for i, c in enumerate(out):
            if c != " ":
                out[i] = chr(mp[ord(c) - 97])
        return "".join(out)
