from typing import List
from collections import defaultdict

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        tree = lambda: defaultdict(tree)
        root = tree()
        for path in paths:
            node = root
            for folder in path:
                node = node[folder]

        # serialize subtree -> mark duplicates
        dup = {}
        serial_of = {}

        def serialize(node) -> str:
            if not node:
                return ""
            parts = []
            for name in sorted(node.keys()):
                parts.append(name + "(" + serialize(node[name]) + ")")
            serial = "".join(parts)
            if serial:
                if serial in dup:
                    dup[serial] = True
                else:
                    dup[serial] = False
                serial_of[id(node)] = serial
            return serial

        serialize(root)

        ans = []

        def collect(node, path):
            for name, child in node.items():
                serial = serial_of.get(id(child), "")
                if serial and dup.get(serial):
                    continue
                path.append(name)
                ans.append(path[:])
                collect(child, path)
                path.pop()

        collect(root, [])
        return ans
